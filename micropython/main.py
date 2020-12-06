import machine,neopixel,time,random,urequests
MAX_FREQ = 160000000 #160Mhz
machine.freq(MAX_FREQ)

class Animate:
    def __init__(self):
        self.count = 300
        self.np = neopixel.NeoPixel(machine.Pin(4), self.count)

    def flowing(self,color_tuple=(0,123,20)):
        for i in range(self.count):
            if (i%2) == 0:
                self.np[i] = color_tuple
            else:
                self.np[i] = (0,0,0)
        self.np.write()
        # time.sleep(0.1)
        for i in range(self.count):
            if (i%2) != 0:
                self.np[i] = color_tuple
            else:
                self.np[i] = (0,0,0)
        self.np.write()
        # time.sleep(0.1)

    def fetch_color(self):
        try:
            r = urequests.get('http://<fetch_color_state_url>/')
            hex_color = r.text.lstrip('#')
            rgb_color = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
            print('Current color is set to: {}'.format(rgb_color))
            return rgb_color #tuple is returned
        except:
            return (0,123,20)

    def run(self):
        while True:
            rgb_color = self.fetch_color()
            for _ in range(10):
                self.flowing(rgb_color)

if __name__ == "__main__":
    time.sleep(60) #wait before wifi successfully connects
    aa = Animate()
    aa.run()
