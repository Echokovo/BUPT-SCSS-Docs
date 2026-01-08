import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class MenuSmile {
    public static void main(String[] args) {
        EventQueue.invokeLater(()->{
            smileFrame s = new smileFrame();
            s.setVisible(true);
        });
    }
}
class smileFrame extends JFrame{
    JPopupMenu popupMenu;
    smilePanel sPanel;
    public smileFrame(){
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setTitle("Smile");
        this.setSize(500,500);
        sPanel = new smilePanel();
        JMenuBar menuBar = new JMenuBar();
        menuBar.add(faceInit());
        menuBar.add(smileInit());
        menuBar.add(helpInit());
        setJMenuBar(menuBar);
        addMouseListener(new MouseAdapter() {
            public void mouseReleased(MouseEvent e) {
                if (e.isPopupTrigger()) {
                    popupMenu.show(e.getComponent(), e.getX(), e.getY());
                }
            }
        });
        add(sPanel);
    }
    private JMenu faceInit(){
        JMenu faceMenu = new JMenu("Face");
        JMenu colorMenu = new JMenu("Color");
        JMenu sizeMenu = new JMenu("Size");
        JMenuItem exitItem = new JMenuItem("Exit");
        JRadioButtonMenuItem yellowItem = new JRadioButtonMenuItem("Yellow");
        JRadioButtonMenuItem pinkItem = new JRadioButtonMenuItem("Pink");
        JRadioButtonMenuItem smallItem = new JRadioButtonMenuItem("Small");
        JRadioButtonMenuItem bigItem = new JRadioButtonMenuItem("Big");
        ButtonGroup colorGroup = new ButtonGroup();
        ButtonGroup sizeGroup = new ButtonGroup();
        ActionListener colorListener = new colorAction();
        ActionListener sizeListener = new sizeAction();

        smallItem.addActionListener(sizeListener);
        bigItem.addActionListener(sizeListener);
        sizeMenu.add(smallItem);
        sizeMenu.add(bigItem);
        sizeGroup.add(smallItem);
        sizeGroup.add(bigItem);
        smallItem.setSelected(true);

        yellowItem.addActionListener(colorListener);
        pinkItem.addActionListener(colorListener);
        colorGroup.add(yellowItem);
        colorGroup.add(pinkItem);
        colorMenu.add(yellowItem);
        colorMenu.add(pinkItem);
        yellowItem.setSelected(true);

        exitItem.addActionListener(new exitAction());

        faceMenu.add(colorMenu);
        faceMenu.add(sizeMenu);
        faceMenu.addSeparator();
        faceMenu.add(exitItem);
        return faceMenu;
    }
    private JMenu smileInit(){
        JMenu smileMenu = new JMenu("Smile");
        JMenuItem smileItem = new JMenuItem("Smile");
        JMenuItem bigsmileItem = new JMenuItem("Bigsmile");
        JMenuItem smileItemPopup = new JMenuItem("Smile");
        JMenuItem bigsmileItemPopup = new JMenuItem("Bigsmile");
        ActionListener smileListener = new smileAction();
        popupMenu = new JPopupMenu();

        smileItem.addActionListener(smileListener);
        bigsmileItem.addActionListener(smileListener);
        smileMenu.add(smileItem);
        smileMenu.add(bigsmileItem);
        smileMenu.addSeparator();

        smileItemPopup.addActionListener(smileListener);
        bigsmileItemPopup.addActionListener(smileListener);
        popupMenu.add(smileItemPopup);
        popupMenu.add(bigsmileItemPopup);

        return smileMenu;
    }
    private JMenu helpInit(){
        JMenu helpMenu = new JMenu("Help");
        JMenuItem indexItem = new JMenuItem("Index");
        JMenuItem aboutItem = new JMenuItem("About");
        helpMenu.add(indexItem);
        helpMenu.add(aboutItem);
        return helpMenu;
    }
    class colorAction implements ActionListener{
        public void actionPerformed(ActionEvent e){
            JRadioButtonMenuItem buttonMenuItem = (JRadioButtonMenuItem) e.getSource();
            String color = buttonMenuItem.getText();
            if(color.equals("Yellow")){
                sPanel.setColor(Color.YELLOW);
            }else{
                sPanel.setColor(Color.PINK);
            }
        }
    }
    class sizeAction implements ActionListener{
        public void actionPerformed(ActionEvent e){
            JRadioButtonMenuItem jrbmi = (JRadioButtonMenuItem) e.getSource();
            String text = jrbmi.getText().toString();
            if(text.equals("Small")){
                setSize(500,500);
            }else{
                setSize(1000,1000);
            }
            
        }
    }
    class smileAction implements ActionListener{
        public void actionPerformed(ActionEvent e){
            JMenuItem jmi = (JMenuItem) e.getSource();
            String text = jmi.getText().toString();
            if(text.equals("Smile")){
                sPanel.state=false;
                sPanel.repaint();
            }else{
                sPanel.state=true;
                sPanel.repaint();
            }
        }
    }
    class exitAction implements ActionListener{
        public void actionPerformed(ActionEvent e){
            System.exit(0);
        }
    }

}
class smilePanel extends JPanel{
    int x;
    int y;
    int width;
    int height;
    boolean state=false;
    Color color;
    public smilePanel(){
        // JButton smile = new JButton("Smile");
        // JButton bigSmile = new JButton("BigSmile");
        // ActionListener al = (ActionEvent e) -> {
        //     JButton temp = (JButton) e.getSource();
        //     state = !temp.getText().equals("Smile");
        //     repaint();
        // };
        color=Color.YELLOW;
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
        // smile.addActionListener(al);
        // bigSmile.addActionListener(al);
        // this.add(smile);
        // this.add(bigSmile);
        this.addKeyListener(kl);
        this.setFocusable(true);
    }
    @Override
    protected void paintComponent(Graphics g){
        super.paintComponent(g);
        Graphics2D g2d = (Graphics2D) g;
        paint(g2d,color);
    }
    protected void paint(Graphics2D g2d,Color color){
        x=getWidth()/4;
        y=getHeight()/4;
        width=getWidth()/2;
        height=getHeight()/2;
        g2d.setColor(color);
        g2d.fillOval(x, y, width, height);
        g2d.setColor(Color.BLACK);
        g2d.fillOval(x+width/4, y+height/4, width/8, height/8);
        g2d.fillOval(x+width*3/5, y+height/4, width/8, height/8);
        g2d.setFont(new Font("Default",Font.BOLD,32));
        if(state){
            g2d.drawString("BigSmiling...", x+width/5, y+height*5/4);
            g2d.fillArc(x+width/8, y, width*3/4, height*7/8, 180, 180);
            g2d.setColor(color);
            g2d.fillArc(x+width/8, y, width*3/4, height*6/8, 180, 180);
        }else{
            g2d.drawString("Smiling...", x+width/5, y+height*5/4);
            g2d.drawArc(x+width/8, y, width*3/4, height*7/8, 180, 180);
        }
    }
    public void setColor(Color color){
        this.color=color;
        repaint();
    }
}