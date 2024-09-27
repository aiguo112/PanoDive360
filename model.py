import segmentation_models_pytorch as smp
from cbam import CBAM

class CustomDeepLabV3Plus(smp.DeepLabV3Plus):
    def __init__(self, encoder_name="resnet34", encoder_weights="imagenet", in_channels=3, classes=11):
        super().__init__(encoder_name=encoder_name, encoder_weights=encoder_weights, in_channels=in_channels, classes=classes)
        self.cbam_low = CBAM(self.encoder.out_channels[-4])
        self.cbam_mid = CBAM(self.encoder.out_channels[-3])
        self.cbam_high = CBAM(self.encoder.out_channels[-2])

    def forward(self, x):
        features = self.encoder(x)
        features[-4] = self.cbam_low(features[-4])
        features[-3] = self.cbam_mid(features[-3])
        features[-2] = self.cbam_high(features[-2])
        decoder_output = self.decoder(*features)
        masks = self.segmentation_head(decoder_output)
        return masks
