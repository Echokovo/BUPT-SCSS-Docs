import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class Smile extends JPanel {
    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        this.setBackground(Color.GRAY);
        g.setColor(Color.YELLOW);
        g.fillOval(50, 50, 200, 200);
        g.setColor(Color.BLACK);
        g.fillOval(90, 100, 30, 30);
        g.fillOval(180, 100, 30, 30);
        g.drawArc(80, 130, 140, 70, 180, 180);
        g.setFont(new Font("Serif", Font.BOLD | Font.ITALIC, 24));
        g.drawString("Smiling...", 110, 270);
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Smile");
        Smile s = new Smile();
        frame.add(s);
        frame.setSize(320, 320);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}