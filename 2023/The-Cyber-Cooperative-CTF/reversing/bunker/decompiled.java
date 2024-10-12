import javax.swing.JOptionPane;
import java.awt.event.ActionEvent;
import java.awt.Component;
import javax.swing.JPanel;
import javax.swing.JButton;
import javax.swing.UIManager;
import javax.swing.JTextField;
import java.awt.event.ActionListener;
import javax.swing.JFrame;

// 
// Decompiled by Procyon v0.6.0
// 

class Bunker extends JFrame implements ActionListener
{
    static JFrame f;
    static JTextField l;
    String output;
    
    Bunker() {
        this.output = "";
    }
    
    public static void main(final String[] array) {
        Bunker.f = new JFrame("Bunker");
        try {
            UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
        }
        catch (final Exception ex) {
            System.err.println(ex.getMessage());
        }
        final Bunker bunker = new Bunker();
        (Bunker.l = new JTextField(8)).setEditable(false);
        final JButton comp = new JButton("0");
        final JButton comp2 = new JButton("1");
        final JButton comp3 = new JButton("2");
        final JButton comp4 = new JButton("3");
        final JButton comp5 = new JButton("4");
        final JButton comp6 = new JButton("5");
        final JButton comp7 = new JButton("6");
        final JButton comp8 = new JButton("7");
        final JButton comp9 = new JButton("8");
        final JButton comp10 = new JButton("9");
        final JPanel comp11 = new JPanel();
        comp.addActionListener(bunker);
        comp2.addActionListener(bunker);
        comp3.addActionListener(bunker);
        comp4.addActionListener(bunker);
        comp5.addActionListener(bunker);
        comp6.addActionListener(bunker);
        comp7.addActionListener(bunker);
        comp8.addActionListener(bunker);
        comp9.addActionListener(bunker);
        comp10.addActionListener(bunker);
        comp11.add(Bunker.l);
        comp11.add(comp);
        comp11.add(comp2);
        comp11.add(comp3);
        comp11.add(comp4);
        comp11.add(comp5);
        comp11.add(comp6);
        comp11.add(comp7);
        comp11.add(comp8);
        comp11.add(comp9);
        comp11.add(comp10);
        Bunker.f.add(comp11);
        Bunker.f.setSize(120, 500);
        Bunker.f.show();
    }
    
    @Override
    public void actionPerformed(final ActionEvent actionEvent) {
        this.output += actionEvent.getActionCommand();
        Bunker.l.setText(this.output);
        if (this.output.length() == 8) {
            System.err.print("USER ENTERED: ");
            System.err.println(this.output);
            Bunker.l.setText("");
            if (this.output.equals("72945810")) {
                final String s = "Q^XSNZD^\\WKk\u0004\tnCVKJkTOPYCm_AGLYUEmPZFLCETFP[[E";
                final StringBuilder sb = new StringBuilder();
                for (int i = 0; i < s.length(); ++i) {
                    sb.append((char)(s.charAt(i) ^ this.output.charAt(i % this.output.length())));
                }
                JOptionPane.showMessageDialog(null, sb.toString());
            }
            else {
                JOptionPane.showMessageDialog(null, "=== BUNKER CODE INVALID ===");
            }
            this.output = "";
        }
    }
}
