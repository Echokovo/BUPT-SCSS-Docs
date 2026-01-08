import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

class Circle extends JFrame {
    private final int d = 100;
    private Color currentColor = Color.WHITE;
    private final JButton[] colors;

    public Circle() {
        setTitle("Circle");
        setSize(400, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel circlePanel = new JPanel() {
            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                Graphics2D g2d = (Graphics2D) g;
                g2d.setColor(currentColor);
                g2d.fillOval((getWidth() - d) / 2, (getHeight() - d) / 2, d, d);
            }
        };
        circlePanel.setPreferredSize(new Dimension(400, 400));
        circlePanel.setBackground(Color.WHITE);

        circlePanel.addMouseMotionListener(new MouseMotionAdapter() {
            @Override
            public void mouseMoved(MouseEvent e) {
                if (check(e.getX(), e.getY())) {
                    circlePanel.setCursor(Cursor.getPredefinedCursor(Cursor.CROSSHAIR_CURSOR));
                } else {
                    circlePanel.setCursor(Cursor.getDefaultCursor());
                }
            }
        });

        circlePanel.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                if (check(e.getX(), e.getY())) {
                    change();
                }
            }
        });

        colors = new JButton[] {
                new JButton("Red"),
                new JButton("Green"),
                new JButton("Blue")
        };

        JPanel buttonPanel = new JPanel();
        for (JButton button : colors) {
            button.addActionListener(e -> {
                String command = e.getActionCommand();
                switch (command) {
                    case "Red":
                        currentColor = Color.RED;
                        break;
                    case "Green":
                        currentColor = Color.GREEN;
                        break;
                    case "Blue":
                        currentColor = Color.BLUE;
                        break;
                }
                repaint();
            });
            buttonPanel.add(button);
        }
        add(buttonPanel, BorderLayout.NORTH);
        add(circlePanel, BorderLayout.CENTER);
    }

    private boolean check(int x, int y) {
        int centerX = getWidth() / 2;
        int centerY = getHeight() / 2;
        int radius = d / 2;
        return Math.pow(x - centerX, 2) + Math.pow(y - centerY, 2) <= Math.pow(radius, 2);
    }

    private void change() {
        if (currentColor == Color.WHITE) {
            currentColor = Color.RED;
        } else if (currentColor == Color.RED) {
            currentColor = Color.GREEN;
        } else if (currentColor == Color.GREEN) {
            currentColor = Color.BLUE;
        } else if (currentColor == Color.BLUE) {
            currentColor = Color.WHITE;
        }
        repaint();
    }

}

public class HW7 {
    public static void main(String[] args) {
        EventQueue.invokeLater(() -> {
            Circle c = new Circle();
            c.setVisible(true);
        });
    }
}