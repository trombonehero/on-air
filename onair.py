# Copyright [yyyy] [name of copyright owner]
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rumps


def find_arduino():
    import glob

    # Find /dev/cu.usbmodem* using the glob module:
    ports = glob.glob('/dev/cu.usbmodem*')
    if len(ports) == 1:
        import nanpy
        return nanpy.ArduinoApi(connection=nanpy.SerialManager(device=ports[0]))

    if len(ports) == 0:
        rumps.notification(title='On Air',
                           subtitle='Error detecting Arduino',
                           message='No Arduino device detected (plugged in?)')
    else:
        rumps.notification(title='On Air',
                           subtitle='Error detecting Arduino',
                           message='Multiple devices detected')


class OnAir:
    def __init__(self):
        self.arduino = find_arduino()
        if self.arduino is None:
            import sys
            sys.exit(1)

        self.on_air = False

        self.app = rumps.App("On Air", "⭕")
        self.toggle = rumps.MenuItem(title='Toggle', callback=self.toggle_light)
        self.app.menu = [self.toggle]

    def toggle_light(self, sender):
        on_air = not self.on_air
        self.app.title = "🔴" if on_air else "⭕"
        self.arduino.analogWrite(4, 255 if on_air else 0)

        self.on_air = on_air

    def run(self):
        self.app.run()


if __name__ == '__main__':
    app = OnAir()
    app.run()
