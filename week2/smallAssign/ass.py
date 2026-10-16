import graphics as g


def main():
    win:g.GraphWin = g.GraphWin("Hello World!", 200, 200)

    win.setBackground("White")
    
    width:float = 100
    height:float = 50
    p1:g.Point = g.Point((200-width)/2, (200-height)/2)
    p2:g.Point = g.Point((200+width)/2, (200+height)/2)
    r: g.Rectangle = g.Rectangle(p1, p2)
    r.setFill(g.color_rgb(157,225,154))
    r.draw(win)

    t:g.Text = g.Text(g.Point(100, 50), "What is up")
    t.setFill(g.color_rgb(188,169,225))
    t.draw(win)

    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()
