import ui


def make_button_item(action, image_name):
    return ui.ButtonItem(action=action, image=ui.Image.named(image_name))


class KitchenHelper(object):
    def __init__(self):
        self.view = ui.load_view('KitchenHelper')
        self.view.present('fullscreen')
        self.view.background_color = "#fcf3d2"
        self.view.name = 'KitchenHelper'
        # header menu
        back = make_button_item(self.bt_back, 'iob:arrow_left_b_32')
        forward = make_button_item(self.bt_forward, 'iob:arrow_right_b_32')
        home = make_button_item(self.bt_home, 'iob:home_32')
        self.view.left_button_items = [back, forward]
        self.view.right_button_items = [home]
        # webview
        self.webview = self.view['webview']
        # TOP View
        self.bt_home(None)

    def bt_back(self, sender):
        self.webview.go_back()
        
    def bt_forward(self, sender):
        self.webview.go_forward()

    def bt_home(self, sender):
        self.webview.load_url('http://google.com')

    def kitchen(self, sender):
        self.webview.load_url('http://365kitchen.net/')

    def cookpad(self, sender):
        self.webview.load_url('http://cookpad.com/')

    def foodgawker(self, sender):
        self.webview.load_url('https://foodgawker.com/')

    def paper(self, sender):
    self.webview.load_url('http://www.shufoo.net/pntweb/shopDetail/264231/')


KitchenHelper()
