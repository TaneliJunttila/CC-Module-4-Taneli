class PredictionClass:
  def __init__(self, model):
    self.model = model

  def predict(self, predictions):
    predictions = self.model.predict(predictions)
    return predictions