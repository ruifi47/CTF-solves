import java.util.Base64;
import java.util.function.IntUnaryOperator;
import java.util.stream.Collectors;

public class JavaRev101 implements IntUnaryOperator {
   public static String fakeFlag = "jctf{red_flags_and_fake_flags_form_an_equivalence_class}";
   public static String reference = "K0c2QjkVcRd1eyFWcUArUDF7NRQwUCp7ckIdR3JRMFdxVz8=";
   private int cnt = 0;

   public static void main(String[] var0) {
      (new JavaRev101()).run(var0);
   }

   public void run(String[] var1) {
      if (var1.length != 1) {
         System.out.println("Usage: java JavaRev101 <flag>");
      } else {
         String var2 = var1[0];
         String var3 = (String)var2.chars().map(this).mapToObj((var0) -> {
            return (new Character((char)var0)).toString();
         }).collect(Collectors.joining(""));
         String var4 = Base64.getEncoder().encodeToString(var3.getBytes());
         if (var4.equals(reference)) {
            System.out.println("You passed this course!");
         } else {
            System.out.println("It seems that you'll need to resit this class...");
         }

      }
   }

   public int applyAsInt(int var1) {
      return var1 ^ (this.cnt++ % 2 == 0 ? 66 : 36);
   }
}
