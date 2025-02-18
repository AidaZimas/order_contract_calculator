from collections import defaultdict

from model.billing import Billing
from model.contract import Contract
from model.current_product import CurrentProduct
from model.disclaimer import Disclaimer
from model.donor_consent import DonorConsent
from model.down_payment import DownPayment
from model.legal import Legal
from model.legal_owner import LegalOwner
from model.monthly_charge import MonthlyCharge
from model.product_details import ProductDetails
from model.service import Service
from model.subscription import Subscription
from model.user import User
from src.model.characteristic import Characteristic
from src.model.flexible_switch import FlexibleSwitch
from src.model.insurance import Insurance
from src.model.monthly_discount import MonthlyDiscount


def to_float(value):
    if value is None:
        return 0.0
    return float(value.replace(',', '.'))


def initialize_subscription(product_data):
    data_dict = {item["NAME"]: item["TEXT_VALUE"] for item in product_data}

    billing = Billing(
        city=data_dict.get("subscriptions[1].billing.city"),
        email=data_dict.get("subscriptions[1].billing.email"),
        firstName=data_dict.get("subscriptions[1].billing.firstName"),
        fullName=data_dict.get("subscriptions[1].billing.fullName"),
        fullStreet=data_dict.get("subscriptions[1].billing.fullStreet"),
        houseNo=data_dict.get("subscriptions[1].billing.houseNo"),
        invoiceEmailAddress=data_dict.get("subscriptions[1].billing.invoiceEmailAddress"),
        invoiceType=data_dict.get("subscriptions[1].billing.invoiceType"),
        lastName=data_dict.get("subscriptions[1].billing.lastName"),
        street=data_dict.get("subscriptions[1].billing.street"),
        zip=data_dict.get("subscriptions[1].billing.zip")
    )

    contract = Contract(
        ban=data_dict.get("subscriptions[1].contract.ban"),
        existingBan=data_dict.get("subscriptions[1].contract.existingBan")
    )

    disclaimers = [
        Disclaimer(text=data_dict.get(f"subscriptions[1].disclaimers[{i}].text"))
        for i in range(1, 3)
    ]

    donor_consent = DonorConsent(
        type=data_dict.get("subscriptions[1].donorConsent.type"),
        value=data_dict.get("subscriptions[1].donorConsent.value"),
        writtenConsentGiven=data_dict.get("subscriptions[1].donorConsent.writtenConsentGiven")
    )

    down_payment = DownPayment(
        downPaymentAmountExVat=to_float(data_dict.get("subscriptions[1].downPayment.downPaymentAmountExVat", "0")),
        downPaymentAmountInVat=to_float(data_dict.get("subscriptions[1].downPayment.downPaymentAmountInVat", "0")),
        installmentAmountExVat=to_float(data_dict.get("subscriptions[1].downPayment.installmentAmountExVat", "0")),
        installmentAmountInVat=to_float(data_dict.get("subscriptions[1].downPayment.installmentAmountInVat", "0")),
        lastInstallmentAmountExVat=to_float(data_dict.get("subscriptions[1].downPayment.lastInstallmentAmountExVat","0")),
        lastInstallmentAmountInVat=to_float(data_dict.get("subscriptions[1].downPayment.lastInstallmentAmountInVat","0")),
        lastInstallmentIsDifferent=data_dict.get("subscriptions[1].downPayment.lastInstallmentIsDifferent") == "true",
        numberOfInstallments=int(data_dict.get("subscriptions[1].downPayment.numberOfInstallments", "0")))

    legal = Legal(
        birthDate=data_dict.get("subscriptions[1].legal.birthDate"),
        city=data_dict.get("subscriptions[1].legal.city"),
        contactPhone=data_dict.get("subscriptions[1].legal.contactPhone"),
        email=data_dict.get("subscriptions[1].legal.email"),
        firstName=data_dict.get("subscriptions[1].legal.firstName"),
        floor=data_dict.get("subscriptions[1].legal.floor"),
        fullName=data_dict.get("subscriptions[1].legal.fullName"),
        fullStreet=data_dict.get("subscriptions[1].legal.fullStreet"),
        houseNo=data_dict.get("subscriptions[1].legal.houseNo"),
        identificationMethodType=data_dict.get("subscriptions[1].legal.identificationMethodType"),
        lastName=data_dict.get("subscriptions[1].legal.lastName"),
        room=data_dict.get("subscriptions[1].legal.room"),
        street=data_dict.get("subscriptions[1].legal.street"),
        zip=data_dict.get("subscriptions[1].legal.zip")
    )

    legal_owner = LegalOwner(
        birthDate=data_dict.get("subscriptions[1].legalOwner.birthDate"),
        city=data_dict.get("subscriptions[1].legalOwner.city"),
        contactPhone=data_dict.get("subscriptions[1].legalOwner.contactPhone"),
        email=data_dict.get("subscriptions[1].legalOwner.email"),
        firstName=data_dict.get("subscriptions[1].legalOwner.firstName"),
        floor=data_dict.get("subscriptions[1].legalOwner.floor"),
        fullName=data_dict.get("subscriptions[1].legalOwner.fullName"),
        fullStreet=data_dict.get("subscriptions[1].legalOwner.fullStreet"),
        houseNo=data_dict.get("subscriptions[1].legalOwner.houseNo"),
        lastName=data_dict.get("subscriptions[1].legalOwner.lastName"),
        room=data_dict.get("subscriptions[1].legalOwner.room"),
        street=data_dict.get("subscriptions[1].legalOwner.street"),
        zip=data_dict.get("subscriptions[1].legalOwner.zip")
    )

    user = User(
        birthDate=data_dict.get("subscriptions[1].user.birthDate"),
        city=data_dict.get("subscriptions[1].user.city"),
        contactPhone=data_dict.get("subscriptions[1].user.contactPhone"),
        email=data_dict.get("subscriptions[1].user.email"),
        fullName=data_dict.get("subscriptions[1].user.fullName"),
        fullStreet=data_dict.get("subscriptions[1].user.fullStreet"),
        houseNo=data_dict.get("subscriptions[1].user.houseNo"),
        street=data_dict.get("subscriptions[1].user.street"),
        zip=data_dict.get("subscriptions[1].user.zip")
    )

    services_dict = defaultdict(dict)
    for item in product_data:
        key, value = item["NAME"], item["TEXT_VALUE"]
        if "subscriptions[1].services[" in key:
            service_index = int(key.split("services[")[1].split("]")[0])
            attribute_name = key.split(f"services[{service_index}].")[1]
            services_dict[service_index][attribute_name] = value

    services = []
    for service_data in services_dict.values():
        flexible_switch = None
        if service_data.get("flexibleSwitch.isTeliaFinance", "false") == "true":
            flexible_switch = FlexibleSwitch(
                downPaymentAmountExVat=float(service_data.get("flexibleSwitch.downPaymentAmountExVat", 0)),
                downPaymentAmountInVat=float(service_data.get("flexibleSwitch.downPaymentAmountInVat", 0)),
                includedInsuranceExVat=float(service_data.get("flexibleSwitch.includedInsuranceExVat", 0)),
                includedInsuranceInVat=float(service_data.get("flexibleSwitch.includedInsuranceInVat", 0)),
                installmentAmountExVat=float(service_data.get("flexibleSwitch.installmentAmountExVat", 0)),
                installmentAmountInVat=float(service_data.get("flexibleSwitch.installmentAmountInVat", 0)),
                isTeliaFinance=True,
                lastInstallmentAmountExVat=float(service_data.get("flexibleSwitch.lastInstallmentAmountExVat", 0)),
                lastInstallmentAmountInVat=float(service_data.get("flexibleSwitch.lastInstallmentAmountInVat", 0)),
                lastInstallmentIsDifferent=service_data.get("flexibleSwitch.lastInstallmentIsDifferent",
                                                            "false") == "true",
                numberOfInstallments=int(service_data.get("flexibleSwitch.numberOfInstallments", 0))
            )
        else:
            flexible_switch = FlexibleSwitch()
        characteristics = []

        for key, value in service_data.items():
            if key.startswith("characteristics[") and key.endswith(".value"):
                index_start = key.find("[") + 1
                index_end = key.find("]")
                characteristic_index = key[index_start:index_end]

                name_key = f"characteristics[{characteristic_index}].name"
                characteristic_name = service_data.get(name_key)

                characteristics.append(Characteristic(name=characteristic_name, value=value))

        services.append(
            Service(
                name=service_data.get("name"),
                action=service_data.get("action"),
                category=service_data.get("category"),
                code=service_data.get("code"),
                classification=service_data.get("classification"),
                lifetimeInMonths=int(service_data.get("lifetimeInMonths", 0)),
                emailAddress=service_data.get("EMAIL_ADDRESS", ""),
                flexibleSwitch=flexible_switch,
                insurance=Insurance(
                    deductibles=service_data.get("insurance.deductibles", ""),
                    securityDirectives=service_data.get("insurance.security.directives", ""),
                    termsType=service_data.get("insurance.terms.type", "")
                ),
                insuranceClass=service_data.get("insuranceClass"),
                customerRelevant = service_data.get("customerRelevant").lower() == "true",
                isSecretNumber=service_data.get("isSecretNumber"),
                monthlyCharge=MonthlyCharge(
                    exVat=to_float(service_data.get("monthlyCharge.exVat")),
                    inVat=to_float(service_data.get("monthlyCharge.inVat"))
                ),
                characteristics=characteristics
            )
        )

    subscription = Subscription(
        id=data_dict.get("subscriptions[1].id"),
        barcode=data_dict.get("subscriptions[1].barcode"),
        billing=billing,
        contract=contract,
        disclaimers=disclaimers,
        donorConsent=donor_consent,
        downPayment=down_payment,
        handset=data_dict.get("subscriptions[1].handset"),
        handsetPrice=to_float(data_dict.get("subscriptions[1].handsetPrice", "0")),
        handsetPriceExVat=to_float(data_dict.get("subscriptions[1].handsetPriceExVat", "0")),
        icc=data_dict.get("subscriptions[1].icc"),
        imei=data_dict.get("subscriptions[1].imei"),
        isNewBan=data_dict.get("subscriptions[1].isNewBan") == "true",
        isNewSubscription=data_dict.get("subscriptions[1].isNewSubscription") == "true",
        isNpTerminationPermitted=data_dict.get("subscriptions[1].isNpTerminationPermitted") == "true",
        isPortingSubscription=data_dict.get("subscriptions[1].isPortingSubscription") == "true",
        isPreToPost=data_dict.get("subscriptions[1].isPreToPost") == "true",
        isPrepaid=data_dict.get("subscriptions[1].isPrepaid") == "true",
        isSimCardHandout=data_dict.get("subscriptions[1].isSimCardHandout") == "true",
        legal=legal,
        legalOwner=legal_owner,
        msisdn=data_dict.get("subscriptions[1].msisdn"),
        npAfterCommitment=data_dict.get("subscriptions[1].npAfterCommitment"),
        npContact=data_dict.get("subscriptions[1].npContact"),
        npDate=data_dict.get("subscriptions[1].npDate"),
        npMsisdn=data_dict.get("subscriptions[1].npMsisdn"),
        npOperator=data_dict.get("subscriptions[1].npOperator"),
        offeringChangeType=data_dict.get("subscriptions[1].offeringChangeType"),
        operation=data_dict.get("subscriptions[1].operation"),
        product=ProductDetails(
            name=data_dict.get("subscriptions[1].product"),
            monthlyDiscount=MonthlyDiscount(
                durationInMonths=to_float(data_dict.get("subscriptions[1].product.monthlyDiscount.durationInMonths")),
                exVat=to_float(data_dict.get("subscriptions[1].product.monthlyDiscount.exVat")),
                inVat=to_float(data_dict.get("subscriptions[1].product.monthlyDiscount.inVat")),
                percentage=to_float(data_dict.get("subscriptions[1].product.monthlyDiscount.percentage"))
            ),
            monthlyCharge=MonthlyCharge(
                exVat=to_float(data_dict.get("subscriptions[1].product.monthlyCharge.exVat")),
                inVat=to_float(data_dict.get("subscriptions[1].product.monthlyCharge.inVat"))
            ),
            offeringDescriptionLong=data_dict.get("subscriptions[1].product.offeringDescriptionLong"),
            offeringDescriptionShort=data_dict.get("subscriptions[1].product.offeringDescriptionShort"),
            shortName=data_dict.get("subscriptions[1].product.shortName"),
            current=CurrentProduct(
                name=data_dict.get("subscriptions[1].product.current"),
                commitmentEnd=data_dict.get("subscriptions[1].product.current.commitmentEnd"),
                commitmentStart=data_dict.get("subscriptions[1].product.current.commitmentStart"),
                disclaimers=[
                    Disclaimer(text=data_dict.get(f"subscriptions[1].product.current.disclaimers[{i}].text"))
                    for i in range(1, 3)
                ],
                hasActiveCommitment=data_dict.get(
                    "subscriptions[1].product.current.hasActiveCommitment") == "true",
                monthlyCharge=MonthlyCharge(
                    exVat=to_float(data_dict.get("subscriptions[1].product.current.monthlyCharge.exVat")),
                    inVat=to_float(data_dict.get("subscriptions[1].product.current.monthlyCharge.inVat"))
                ),
                offeringDescriptionLong=data_dict.get(
                    "subscriptions[1].product.current.offeringDescriptionLong"),
                offeringDescriptionShort=data_dict.get(
                    "subscriptions[1].product.current.offeringDescriptionShort"),
                shortName=data_dict.get("subscriptions[1].product.current.shortName")
            ),
            disclaimers=[
                Disclaimer(text=data_dict.get(f"subscriptions[1].product.disclaimers[{i}].text"))
                for i in range(1, 3)
            ]
        ),
        resultingServices=data_dict.get("subscriptions[1].resultingServices", "").split(","),
        services=services,
        simType=data_dict.get("subscriptions[1].simType"),
        user=user
    )

    return subscription
