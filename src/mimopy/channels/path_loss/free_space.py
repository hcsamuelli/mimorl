from numpy import pi
from ..awgn import Channel
from .path_loss import PathLoss


class FreeSpaceLoss(PathLoss):
    """Free-space path loss model for isotropic antennas."""

    def received_power(self, channel:Channel):
        """
        Calculate the received power at the receiver.

        P_{\mathrm{rx}}=\\frac{P_{\mathrm{tx}}}{4 \pi d^2} \cdot A_{\mathrm{eff}},
        A_{\mathrm{eff}}=\\frac{\lambda^2}{4 \pi}.
        """
        d = channel.get_relative_position(channel.tx, channel.rx)
        # the distance is calculated in wavelength so the wl term is not needed
        return channel.tx.power / (16 * pi ** 2 * d**2)