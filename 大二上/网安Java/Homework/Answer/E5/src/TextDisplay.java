
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;
import javax.swing.*;
import static javax.swing.WindowConstants.EXIT_ON_CLOSE;

public class TextDisplay {
    public static void main(String[] args) throws Exception {
        EventQueue.invokeLater(() ->{
            menuFrame frame = new menuFrame();
            frame.setDefaultCloseOperation(EXIT_ON_CLOSE);
            //frame.setSize(800,600);
            frame.pack();
            frame.setVisible(true);
        });
    }
}
class menuFrame extends JFrame{
    public menuFrame(){
        setLayout(new BorderLayout(0,0));
        setTitle("TextDisplay");
        textPanel tPanel = new textPanel();
        buttonPanel bPanel = new buttonPanel(tPanel);
        setFontPanel sfPanel = new setFontPanel(tPanel);
        add(sfPanel,BorderLayout.NORTH);
        add(tPanel,BorderLayout.CENTER);
        add(bPanel,BorderLayout.SOUTH);
    }
}
class setFontPanel extends JPanel{
    textPanel tPanel;
    public setFontPanel(textPanel tPanel){
        this.tPanel=tPanel;
        GridBagLayout gbl = new GridBagLayout();
        GridBagConstraints gbc = new GridBagConstraints();
        setLayout(gbl);
        gbc.fill = GridBagConstraints.BOTH;

        JLabel fontLabel = new JLabel("Font");
        JComboBox fontComboBox = new JComboBox();
        fontComboBox.addItem("Serif");
        fontComboBox.addItem("仿宋");
        fontComboBox.addItemListener(new fontAction());
        setPos(gbc, gbl, fontLabel, 0, 0, 1, 1);
        setPos(gbc, gbl, fontComboBox, 1, 0, 0, 1);
        add(fontLabel);
        add(fontComboBox);
        
        JCheckBox boldCheckBox = new JCheckBox("Bold");
        JCheckBox italiCheckBox = new JCheckBox("Italic");
        boldCheckBox.addActionListener(new styleAction());
        italiCheckBox.addActionListener(new styleAction());
        setPos(gbc, gbl, boldCheckBox, 0, 1, 2, 1);
        setPos(gbc, gbl, italiCheckBox, 2, 1, 2, 1);
        add(boldCheckBox);
        add(italiCheckBox);

        ButtonGroup group = new ButtonGroup();
        JRadioButton smallButton = new JRadioButton("Small");
        JRadioButton mediumButton = new JRadioButton("Medium");
        JRadioButton largeButton = new JRadioButton("Large");
        JRadioButton extralargeButton = new JRadioButton("Extra large");
        mediumButton.setSelected(true);
        smallButton.addActionListener(new sizeAction());
        mediumButton.addActionListener(new sizeAction());
        largeButton.addActionListener(new sizeAction());
        extralargeButton.addActionListener(new sizeAction());
        group.add(smallButton);
        group.add(mediumButton);
        group.add(largeButton);
        group.add(extralargeButton);
        setPos(gbc, gbl, smallButton, 0, 3, 1, 1);
        setPos(gbc, gbl, mediumButton, 1, 3, 1, 1);
        setPos(gbc, gbl, largeButton, 2, 3, 1, 1);
        setPos(gbc, gbl, extralargeButton, 3, 3, 1, 1);
        add(smallButton);
        add(mediumButton);
        add(largeButton);
        add(extralargeButton);
    }
    private void setPos(GridBagConstraints gbc,GridBagLayout gbl,Component c,int x,int y,int w,int h){
        gbc.gridx = x;
        gbc.gridy = y;
        gbc.gridwidth = w;
        gbc.gridheight = h;
        gbl.setConstraints(c, gbc);
    }
    private class fontAction implements ItemListener{
        public void itemStateChanged(ItemEvent e) {
            if(e.getStateChange()==ItemEvent.SELECTED){
                JComboBox comboBox = (JComboBox) e.getSource();
                String fontName = (String) comboBox.getSelectedItem();
                tPanel.resetFont(fontName);
            }
        }
    }
    private class styleAction implements ActionListener{
        public void actionPerformed(ActionEvent e) {
            JCheckBox checkBox = (JCheckBox) e.getSource();
            if (checkBox.getText().equals("Bold")) {
                tPanel.resetBold(checkBox.isSelected());
            } else if (checkBox.getText().equals("Italic")) {
                tPanel.resetItalic(checkBox.isSelected());
            }
        }
    }
    private class sizeAction implements ActionListener{
        public void actionPerformed(ActionEvent e) {
            JRadioButton radioButton = (JRadioButton) e.getSource();
            String text = radioButton.getText();
            int size;
            size = switch (text) {
                case "Small" -> 10;
                case "Medium" -> 15;
                case "Large" -> 20;
                case "Extra large" -> 25;
                default -> 15;
            };
            tPanel.resetSize(size);
        }
    }
}
class textPanel extends JPanel{
    JTextArea textArea;
    String text;
    Font f;
    public textPanel() {
        text="";
        f = new Font("Serif",0,15);
        textArea = new JTextArea(text, 10, 30);
        textArea.setFont(f);
        textArea.setLineWrap(true);
        add(textArea);
    }
    public void add(){
        text+="The quick brown fox jumps over the lazy dog.\n";
        textArea.setText(text);
    }
    public void clean(){
        text="";
        textArea.setText(text);
    }
    public void resetFont(String fontName){
        f = new Font(fontName,f.getStyle(),f.getSize());
        textArea.setFont(f);
    }
    public void resetStyle(int style){
        f = new Font(f.getFamily(),style,f.getSize());
        textArea.setFont(f);
    }
    public void resetBold(boolean isBold) {
        int style = f.getStyle();
        if (isBold) {
            style |= Font.BOLD;
        } else {
            style &= ~Font.BOLD;
        }
        resetStyle(style);
    }
    public void resetItalic(boolean isItalic) {
        int style = f.getStyle();
        if (isItalic) {
            style |= Font.ITALIC;
        } else {
            style &= ~Font.ITALIC;
        }
        resetStyle(style);
    }
    public void resetSize(int fontSize){
        f = new Font(f.getFamily(),f.getStyle(),fontSize);
        textArea.setFont(f);
    }
}
class buttonPanel extends JPanel{
    textPanel tPanel;
    public buttonPanel(textPanel tPanel){
        this.tPanel=tPanel;
        JButton insertButton = new JButton("Insert");
        JButton cleanButton = new JButton("Clean");
        insertButton.addActionListener(new insertAction());
        cleanButton.addActionListener(new cleanAction());
        add(insertButton);
        add(cleanButton);
    }
    private class insertAction implements ActionListener{
        public void actionPerformed(ActionEvent e) {
            tPanel.add();
        }
    }
    private class cleanAction implements ActionListener{
        public void actionPerformed(ActionEvent e) {
            tPanel.clean();
        }
    }
}