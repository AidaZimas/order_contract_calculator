class DownPayment:
    def __init__(self, downPaymentAmountExVat=0.0, downPaymentAmountInVat=0.0, installmentAmountExVat=0.0, installmentAmountInVat=0.0, lastInstallmentAmountExVat=0.0, lastInstallmentAmountInVat=0.0, lastInstallmentIsDifferent=False, numberOfInstallments=0):
        self.downPaymentAmountExVat = downPaymentAmountExVat
        self.downPaymentAmountInVat = downPaymentAmountInVat
        self.installmentAmountExVat = installmentAmountExVat
        self.installmentAmountInVat = installmentAmountInVat
        self.lastInstallmentAmountExVat = lastInstallmentAmountExVat
        self.lastInstallmentAmountInVat = lastInstallmentAmountInVat
        self.lastInstallmentIsDifferent = lastInstallmentIsDifferent
        self.numberOfInstallments = numberOfInstallments