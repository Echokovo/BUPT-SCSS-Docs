import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import javax.swing.*;

public class Smile {
    public static void main(String[] args) {
        EventQueue.invokeLater(()->{
            smileFrame s = new smileFrame();
            s.setVisible(true);
        });
    }
}
class smileFrame extends JFrame{
    public smileFrame(){
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setTitle("Smile");
        this.setSize(500,500);
        this.add(new smilePanel());
    }
}
class smilePanel extends JPanel{
    int x;
    int y;
    int width;
    int height;
    boolean state=false;
    public smilePanel(){
        JButton smile = new JButton("Smile");
        JButton bigSmile = new JButton("BigSmile");
        ActionListener al = (ActionEvent e) -> {
            JButton temp = (JButton) e.getSource();
            state = !temp.getText().equals("Smile");
            repaint();
        };
        KeyListener kl = new KeyAdapter() {
            @Override
            public void keyPressed(KeyEvent e) {
                if (e.isControlDown() && e.getKeyCode() == KeyEvent.VK_B) {
                    state=true;
                    repaint();
                }
                if (e.isControlDown() && e.getKeyCode() == KeyEvent.VK_L) {
                    state=false;
                    repaint();
                }
            }
        };
        smile.addActionListener(al);
        bigSmile.addActionListener(al);
        this.add(smile);
        this.add(bigSmile);
        this.addKeyListener(kl);
        this.setFocusable(true);
    }
    @Override
    protected void paintComponent(Graphics g){
        super.paintComponent(g);
        Graphics2D g2d = (Graphics2D) g;
        x=getWidth()/4;
        y=getHeight()/4;
        width=getWidth()/2;
        height=getHeight()/2;
        g2d.setColor(Color.YELLOW);
        g2d.fillOval(x, y, width, height);
        g2d.setColor(Color.BLACK);
        g2d.fillOval(x+width/4, y+height/4, width/8, height/8);
        g2d.fillOval(x+width*3/5, y+height/4, width/8, height/8);
        g2d.setFont(new Font("Default",Font.BOLD,32));
        if(state){
            g2d.drawString("BigSmiling...", x+width/5, y+height*5/4);
            g2d.fillArc(x+width/8, y, width*3/4, height*7/8, 180, 180);
            g2d.setColor(Color.YELLOW);
            g2d.fillArc(x+width/8, y, width*3/4, height*6/8, 180, 180);
        }else{
            g2d.drawString("Smiling...", x+width/5, y+height*5/4);
            g2d.drawArc(x+width/8, y, width*3/4, height*7/8, 180, 180);
        }
    }
}