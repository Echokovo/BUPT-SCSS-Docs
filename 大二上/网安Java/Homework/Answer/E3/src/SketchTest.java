import java.awt.*;
import java.awt.event.*;
import java.awt.geom.*;
import java.util.*;
import javax.swing.*;
public class SketchTest {
	public static void main(String[] args){
		SketchFrame f = new SketchFrame();
		f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		f.setVisible(true);
	}
}

class SketchFrame extends JFrame{
	public SketchFrame(){
		this.setTitle("Sketch Frame");
		this.setSize(DEFAULT_WIDTH,DEFAULT_HEIGHT);
		this.add(new SketchPanel());
	}
	
	public static final int DEFAULT_WIDTH = 400;
	public static final int DEFAULT_HEIGHT = 300;

}

class SketchPanel extends JPanel{
	public SketchPanel(){
		pl = new ArrayList<Line2D>();
		last = new Point2D.Double(100, 100);
		System.out.println(this.getWidth());
		System.out.println(this.getHeight());
		KeyHandler h = new KeyHandler();
		MouseHandler m = new MouseHandler();
		this.addKeyListener(h);
		this.addMouseListener(m);
		this.setFocusable(true);
		
	}
	public void paintComponent(Graphics g){
		Graphics2D g2 = (Graphics2D)g;
		super.paintComponent(g2);
		
		for(Line2D l:pl){
			g2.draw(l);
		}
	
	}
	public void add(int dx, int dy){
		
		Point2D end = new Point2D.Double(last.getX()+dx,last.getY()+dy);
		Line2D l = new Line2D.Double(last,end);
		pl.add(l);
		
		last = end;
		
		repaint();		
	}
	
	private class KeyHandler implements KeyListener{
	 public void keyPressed(KeyEvent ke){
		 System.out.println("key pressed");
		 int c = ke.getKeyCode();
		 int d;
		 if(ke.isShiftDown())
			 d = LARGE_INCRE;
		 else
			 d = SMALL_INCRE;
		 
		 if(c == KeyEvent.VK_LEFT) add(-d,0);
		 else if(c == KeyEvent.VK_RIGHT) add(d,0);
		 else if(c == KeyEvent.VK_UP)	add(0,-d);
		 else if(c == KeyEvent.VK_DOWN) add(0,d);
	 }
	 
	 public void keyReleased(KeyEvent ke){
		 System.out.println("key released");
		 
	 }
	 public void keyTyped(KeyEvent ke){
		 System.out.println("key typed");
		 char ch = ke.getKeyChar();
		 int d;
		 if(Character.isUpperCase(ch)){
			 d = LARGE_INCRE;
			 ch = Character.toLowerCase(ch);
		 }
		 else
			 d = SMALL_INCRE;
		 
		 if( ch == 'h') add(-d,0);
		 else if (ch == 'l') add(d,0);
		 else if(ch == 'k')  add(0,-d);
		 else if(ch == 'j')  add(0,d);
		 
	 }
	}
	private class MouseHandler implements MouseListener{

        @Override
        public void mouseClicked(MouseEvent e) {
            last=e.getPoint();
        }

        @Override
        public void mousePressed(MouseEvent e) {
            
        }

        @Override
        public void mouseReleased(MouseEvent e) {
            
        }

        @Override
        public void mouseEntered(MouseEvent e) {
            
        }

        @Override
        public void mouseExited(MouseEvent e) {
            
        }
		
	}
	
	public static final int SMALL_INCRE = 1;
	public static final int LARGE_INCRE = 5;
	private ArrayList<Line2D> pl;
	private Point2D last;
}
