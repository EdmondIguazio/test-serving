from dir1.dir2.func import func

import mlrun.serving

class SlotFillerServe(mlrun.serving.V2ModelServer):

    def load(self):
        pass

    def predict(self, body):
        return 1
