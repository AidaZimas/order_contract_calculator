class FlexibleSwitch:
    def __init__(self,
                 downPaymentAmountExVat=0.0,
                 downPaymentAmountInVat=0.0,
                 includedInsuranceExVat=0.0,
                 includedInsuranceInVat=0.0,
                 installmentAmountExVat=0.0,
                 installmentAmountInVat=0.0,
                 isTeliaFinance=False,
                 lastInstallmentAmountExVat=0.0,
                 lastInstallmentAmountInVat=0.0,
                 lastInstallmentIsDifferent=False,
                 numberOfInstallments=0):
        self.downPaymentAmountExVat = downPaymentAmountExVat
        self.downPaymentAmountInVat = downPaymentAmountInVat
        self.includedInsuranceExVat = includedInsuranceExVat
        self.includedInsuranceInVat = includedInsuranceInVat
        self.installmentAmountExVat = installmentAmountExVat
        self.installmentAmountInVat = installmentAmountInVat
        self.isTeliaFinance = isTeliaFinance
        self.lastInstallmentAmountExVat = lastInstallmentAmountExVat
        self.lastInstallmentAmountInVat = lastInstallmentAmountInVat
        self.lastInstallmentIsDifferent = lastInstallmentIsDifferent
        self.numberOfInstallments = numberOfInstallments