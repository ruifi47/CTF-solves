import("CoreLibs/string")
local g = playdate.graphics
local geom = playdate.geometry
local trimWhitespace = playdate.string.trimWhitespace
local trimTrailingWhitespace = playdate.string.trimTrailingWhitespace
local PI = 3.1415927
local TWO_PI = 6.2831855
function playdate.graphics.drawCircleInRect(x, ...)
	local y, w, h, lineWidth
	if type(x) == "userdata" then
		x, y, w, h = x.x, x.y, x.width, x.height
	else
		y, w, h = select(1, ...)
	end
	if w > h then
		x = x + (w - h) / 2
		w = h
	elseif h > w then
		y = y + (h - w) / 2
		h = w
	end
	g.drawEllipseInRect(x, y, w, h)
end
function playdate.graphics.fillCircleInRect(x, ...)
	local y, w, h
	if type(x) == "userdata" then
		x, y, w, h = x.x, x.y, x.width, x.height
	else
		y, w, h = select(1, ...)
	end
	if w > h then
		x = x + (w - h) / 2
		w = h
	elseif h > w then
		y = y + (h - w) / 2
		h = w
	end
	g.fillEllipseInRect(x, y, w, h)
end
function playdate.graphics.drawCircleAtPoint(x, ...)
	local y, radius, lineWidth
	if type(x) == "userdata" then
		x, y = x.x, x.y
		radius = select(1, ...)
	else
		y, radius = select(1, ...)
	end
	local d = radius * 2
	g.drawEllipseInRect(x - radius, y - radius, d, d)
end
function playdate.graphics.fillCircleAtPoint(x, ...)
	local y, radius
	if type(x) == "userdata" then
		x, y = x.x, x.y
		radius = select(1, ...)
	else
		y, radius = select(1, ...)
	end
	local d = radius * 2
	g.fillEllipseInRect(x - radius, y - radius, d, d)
end
local lineWidthNag = true
function playdate.graphics.drawArc(x, ...)
	local y, radius, startAngle, endAngle, tempLineWidth
	if type(x) == "userdata" then
		x, y, radius, startAngle, endAngle = x.x, x.y, x.radius, x.startAngle, x.endAngle
		tempLineWidth = select(1, ...)
	else
		y, radius, startAngle, endAngle, tempLineWidth = select(1, ...)
	end
	if true == lineWidthNag and nil ~= tempLineWidth then
		print("Warning: playdate.graphics.drawRoundRect no longer accepts a lineWidth argument, please set the line width using playdate.graphics.setLineWidth() instead")
		lineWidthNag = false
	end
	local d = radius * 2
	g.drawEllipseInRect(x - radius, y - radius, d, d, startAngle, endAngle)
end
local deg = math.deg
local atan2 = math.atan2
function playdate.graphics.drawSineWave(x1, y1, x2, y2, a1, a2, p, ps)
	assert(p > 0, "period must be > 0")
	local r = math.deg(math.atan2(y2 - y1, x2 - x1))
	local lp_sin = function(x)
		if x < -PI then
			x = x + TWO_PI
		elseif x > PI then
			x = x - TWO_PI
		end
		if x < 0 then
			return 1.2732395 * x + 0.40528473 * x * x
		else
			return 1.2732395 * x - 0.40528473 * x * x
		end
	end
	local points = {}
	local xspacing = 3
	local w = geom.distanceToPoint(x1, y1, x2, y2)
	local theta = 0
	if nil ~= ps then
		theta = TWO_PI * (ps % p / p)
	end
	local delta = TWO_PI / p * xspacing
	local x = 0
	local y = lp_sin(theta) * a1
	points[#points + 1] = x
	points[#points + 1] = y
	for _ = xspacing, w, xspacing do
		local ia = a1 + (a2 - a1) * (x / w)
		y = lp_sin(theta) * ia
		points[#points + 1] = x
		points[#points + 1] = y
		x = x + xspacing
		theta = theta + delta
		if theta > TWO_PI then
			theta = theta - TWO_PI
		end
	end
	theta = TWO_PI * (w % p / p)
	y = lp_sin(theta) * a2
	points[#points + 1] = w
	points[#points + 1] = y
	local poly = geom.polygon.new(table.unpack(points))
	local af = geom.affineTransform.new()
	if 0 ~= r then
		af:rotate(r)
	end
	af:translate(x1, y1)
	af:transformPolygon(poly)
	g.drawPolygon(poly)
end
function playdate.graphics.image:drawAnchored(x, y, cx, cy, flip)
	local w, h = self:getSize()
	self:draw(x - cx * w, y - cy * h, flip)
end
function playdate.graphics.image:drawCentered(x, y, flip)
	local w, h = self:getSize()
	self:draw(x - w * 0.5, y - h * 0.5, flip)
end
kTextAlignment = {
	left = 0,
	right = 1,
	center = 2
}
local _styleCharacterForNewline = function(line)
	local _, boldCount = string.gsub(line, "*", "*")
	if 0 ~= boldCount % 2 then
		return "*"
	end
	local _, italicCount = string.gsub(line, "_", "_")
	if 0 ~= italicCount % 2 then
		return "_"
	end
	return ""
end
local _addStyleToLine = function(style, line)
	if 0 == #style then
		return line
	elseif line:sub(1, 1) == style then
		return line:sub(2, -1)
	else
		return style .. line
	end
end
local _layoutTextInRect = function(shouldDrawText, str, x, ...)
	if nil == str then
		return 0, 0, false, nil
	end
	local y, width, height, lineHeightAdjustment, truncator, textAlignment, singleFont, returnStringInfo
	if type(x) == "userdata" then
		x, y, width, height = x.x, x.y, x.width, x.height
		lineHeightAdjustment, truncator, textAlignment, singleFont, returnStringInfo = select(1, ...)
	else
		y, width, height, lineHeightAdjustment, truncator, textAlignment, singleFont, returnStringInfo = select(1, ...)
	end
	local stringInfo
	if true == returnStringInfo then
		stringInfo = {}
		stringInfo.textAlignment = textAlignment
		stringInfo.singleFont = singleFont
	end
	if width < 0 or height < 0 then
		return 0, 0, false, nil
	end
	local font
	if nil == singleFont then
		font = g.getFont()
		if nil == font then
			print("error: no font set!")
			return 0, 0, false, nil
		end
	end
	y = math.floor(y)
	x = math.floor(x)
	lineHeightAdjustment = math.floor(lineHeightAdjustment or 0)
	if nil == truncator then
		truncator = ""
	end
	local top = y
	local bottom = y + height
	local currentLine = ""
	local lineWidth = 0
	local firstWord = true
	local lineHeight, fontLeading, fontHeight
	if nil == singleFont then
		fontLeading = font:getLeading()
		fontHeight = font:getHeight()
		lineHeight = fontHeight + fontLeading
	else
		fontLeading = singleFont:getLeading()
		fontHeight = singleFont:getHeight()
		lineHeight = fontHeight + fontLeading
	end
	local maxLineWidth = 0
	if height < fontHeight then
		return 0, 0, false
	else
		lineHeight = lineHeight + lineHeightAdjustment
	end
	local getLineWidth = function(text)
		if nil == singleFont then
			return g.getTextSize(text)
		else
			return singleFont:getTextWidth(text)
		end
	end
	local drawAlignedText = function(t, twidth)
		if twidth > maxLineWidth then
			maxLineWidth = twidth
		end
		if nil ~= stringInfo then
			stringInfo[#stringInfo + 1] = {
				text = t,
				width = twidth,
				y = y
			}
		end
		if false == shouldDrawText then
			return
		end
		local alignedX = x
		if textAlignment == kTextAlignment.right then
			alignedX = x + width - twidth
		elseif textAlignment == kTextAlignment.center then
			alignedX = x + (width - twidth) / 2
		end
		if nil == singleFont then
			g.drawText(t, alignedX, y)
		else
			singleFont:drawText(t, alignedX, y)
		end
	end
	local drawTruncatedWord = function(wordLine)
		lineWidth = getLineWidth(wordLine)
		local truncatedWord = wordLine
		local stylePrefix = _styleCharacterForNewline(truncatedWord)
		while lineWidth > width and #truncatedWord > 1 do
			truncatedWord = truncatedWord:sub(1, -2)
			lineWidth = getLineWidth(truncatedWord)
		end
		drawAlignedText(truncatedWord, lineWidth)
		local remainingWord = _addStyleToLine(stylePrefix, wordLine:sub(#truncatedWord + 1, -1))
		lineWidth = getLineWidth(remainingWord)
		firstWord = true
		return remainingWord
	end
	local drawTruncatedLine = function()
		currentLine = trimTrailingWhitespace(currentLine)
		lineWidth = getLineWidth(currentLine .. truncator)
		while lineWidth > width and getLineWidth(currentLine) > 0 do
			currentLine = currentLine:sub(1, -2)
			lineWidth = getLineWidth(currentLine .. truncator)
		end
		currentLine = currentLine .. truncator
		lineWidth = getLineWidth(currentLine)
		firstWord = true
		drawAlignedText(currentLine, lineWidth)
		local textBlockHeight = y - top + fontHeight
		return maxLineWidth, textBlockHeight, true, stringInfo
	end
	local drawLineAndMoveToNext = function(firstWordOfNextLine)
		firstWordOfNextLine = _addStyleToLine(_styleCharacterForNewline(currentLine), firstWordOfNextLine)
		drawAlignedText(currentLine, lineWidth)
		y = y + lineHeight
		currentLine = firstWordOfNextLine
		lineWidth = getLineWidth(firstWordOfNextLine)
		firstWord = true
	end
	local lines = {}
	local i = 1
	for line in str:gmatch("[^\r\n]*") do
		lines[i] = line
		i = i + 1
	end
	local line
	for i = 1, #lines do
		line = lines[i]
		local firstWordInLine = true
		local leadingWhiteSpace = ""
		for word in line:gmatch("%S+ *") do
			if true == firstWordInLine then
				local leadingSpace = line:match("^%s+")
				if nil ~= leadingSpace then
					leadingWhiteSpace = leadingSpace
				end
				firstWordInLine = false
			else
				leadingWhiteSpace = ""
			end
			if firstWord then
				if #currentLine > 0 then
					while width < getLineWidth(leadingWhiteSpace .. currentLine) do
						currentLine = drawTruncatedWord(leadingWhiteSpace .. currentLine)
						y = y + lineHeight
					end
				else
					word = leadingWhiteSpace .. word
					while width < getLineWidth(word) do
						if bottom >= y + fontHeight then
							if bottom >= y + lineHeight + fontHeight then
								word = drawTruncatedWord(leadingWhiteSpace .. word)
							else
								currentLine = word
								return drawTruncatedLine()
							end
							leadingWhiteSpace = ""
						end
						y = y + lineHeight
					end
				end
				firstWord = false
			end
			if width >= getLineWidth(currentLine .. leadingWhiteSpace .. trimWhitespace(word)) then
				currentLine = currentLine .. leadingWhiteSpace .. word
			elseif bottom >= y + lineHeight + fontHeight then
				currentLine = leadingWhiteSpace .. trimTrailingWhitespace(currentLine)
				lineWidth = getLineWidth(currentLine)
				drawLineAndMoveToNext(leadingWhiteSpace .. word)
			else
				currentLine = leadingWhiteSpace .. currentLine .. word
				if bottom >= y + fontHeight then
					return drawTruncatedLine()
				end
				local textBlockHeight = y - top + fontHeight
				return maxLineWidth, textBlockHeight, true, stringInfo
			end
		end
		if nil == lines[i + 1] or bottom >= y + lineHeight + fontHeight then
			if #currentLine > 0 then
				while width < getLineWidth(currentLine) do
					currentLine = drawTruncatedWord(currentLine)
					y = y + lineHeight
				end
			end
			lineWidth = getLineWidth(currentLine)
			drawLineAndMoveToNext("")
		else
			return drawTruncatedLine()
		end
	end
	local textBlockHeight = y - top - lineHeight + fontHeight
	return maxLineWidth, textBlockHeight, false, stringInfo
end
function playdate.graphics.drawTextInRect(str, x, ...)
	return _layoutTextInRect(true, str, x, ...)
end
function playdate.graphics.getTextSizeForMaxWidth(str, maxWidth, lineHeightAdjustment, singleFont)
	local w, h, _ = _layoutTextInRect(false, str, 0, 0, maxWidth, math.maxinteger, lineHeightAdjustment or 0, "", kTextAlignment.left, singleFont)
	return w, h
end
function playdate.graphics.imageWithText(str, maxWidth, maxHeight, bgColor, lineHeightAdjustment, truncator, textAlignment, singleFont)
	if nil == maxHeight then
		maxHeight = math.maxinteger
	end
	if nil == bgColor then
		bgColor = g.kColorClear
	end
	local w, h, truncated, textInfo = _layoutTextInRect(false, str, 0, 0, maxWidth, maxHeight, lineHeightAdjustment, truncator, textAlignment, singleFont, true)
	if nil == textInfo then
		return nil, false
	end
	local textAlignment = textInfo.textAlignment
	local singleFont = textInfo.singleFont
	local img = g.image.new(w, h, bgColor)
	g.lockFocus(img)
	local drawAlignedText = function(t, y, twidth)
		local alignedX = 0
		if textAlignment == kTextAlignment.right then
			alignedX = w - twidth
		elseif textAlignment == kTextAlignment.center then
			alignedX = (w - twidth) // 2
		end
		if nil == singleFont then
			g.drawText(t, alignedX, y)
		else
			singleFont:drawText(t, alignedX, y)
		end
	end
	local i, line
	for i = 1, #textInfo do
		line = textInfo[i]
		drawAlignedText(line.text, line.y, line.width)
	end
	g.unlockFocus()
	return img, truncated
end
function playdate.graphics.drawTextAligned(str, x, y, textAlignment, lineHeightAdjustment)
	local font = g.getFont()
	if nil == font then
		print("error: no font set!")
		return 0, 0
	end
	local lineHeight = font:getHeight() + font:getLeading() + math.floor(lineHeightAdjustment or 0)
	local ox = x
	str = "" .. str
	local styleCharacterForNewline = ""
	for line in str:gmatch("[^\r\n]*") do
		line = _addStyleToLine(styleCharacterForNewline, line)
		local width = g.getTextSize(line)
		if textAlignment == kTextAlignment.right then
			x = ox - width
		elseif textAlignment == kTextAlignment.center then
			x = ox - width / 2
		end
		g.drawText(line, x, y)
		y = y + lineHeight
		styleCharacterForNewline = _styleCharacterForNewline(line)
	end
end
function playdate.graphics.font:drawTextAligned(str, x, y, textAlignment, lineHeightAdjustment)
	local lineHeight = self:getHeight() + self:getLeading() + math.floor(lineHeightAdjustment or 0)
	local ox = x
	str = "" .. str
	for line in str:gmatch("[^\r\n]*") do
		local width = self:getTextWidth(line)
		if textAlignment == kTextAlignment.right then
			x = ox - width
		elseif textAlignment == kTextAlignment.center then
			x = ox - width / 2
		end
		self:drawText(line, x, y)
		y = y + lineHeight
	end
end
function playdate.graphics.drawLocalizedTextAligned(text, x, y, alignment, language, lineHeightAdjustment)
	local localizedText = g.getLocalizedText(text, language)
	g.drawTextAligned(localizedText, x, y, alignment, lineHeightAdjustment)
end
function playdate.graphics.drawLocalizedTextInRect(text, x, ...)
	local index
	if type(x) == "userdata" then
		index = 4
	else
		index = 7
	end
	local font, language = select(index, ...)
	local args = table.pack(...)
	if nil == language and type(font) == "number" or type(font) == "string" then
		language = font
		font = nil
		table.remove(args, index)
	end
	local localizedText = g.getLocalizedText(text, language)
	g.drawTextInRect(localizedText, x, table.unpack(args))
end
