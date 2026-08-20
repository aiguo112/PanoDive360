import segmentation_models_pytorch as smp

from panodive360.models.erp_cbam import ERP_CBAM


class DeepLabV3PlusERPCBAM(smp.DeepLabV3Plus):
    """DeepLabv3+ with latitude-weighted ERP-CBAM on encoder features."""

    def __init__(self, encoder_name='resnet34', encoder_weights='imagenet', in_channels=3, classes=11):
        super().__init__(
            encoder_name=encoder_name,
            encoder_weights=encoder_weights,
            in_channels=in_channels,
            classes=classes,
        )
        self.cbam_low = ERP_CBAM(self.encoder.out_channels[-4])
        self.cbam_mid = ERP_CBAM(self.encoder.out_channels[-3])
        self.cbam_high = ERP_CBAM(self.encoder.out_channels[-2])

    def forward(self, x):
        features = self.encoder(x)
        features[-4] = self.cbam_low(features[-4])
        features[-3] = self.cbam_mid(features[-3])
        features[-2] = self.cbam_high(features[-2])
        decoder_output = self.decoder(*features)
        masks = self.segmentation_head(decoder_output)
        return masks


# Name used in the original scripts
CustomDeepLabV3Plus = DeepLabV3PlusERPCBAM
