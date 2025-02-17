from collections import defaultdict
from model.current_product import CurrentProduct
from model.legal_owner import LegalOwner
from model.monthly_charge import MonthlyCharge
from model.product_details import ProductDetails
from model.subscription import Subscription
from model.service import Service

from model.billing import Billing
from model.contract import Contract
from model.disclaimer import Disclaimer
from model.donor_consent import DonorConsent
from model.down_payment import DownPayment
from model.legal import Legal

from model.user import User
from switch import Switch

def initialize_subscription(product_data):
    product_data_dict = {item["NAME"]: item["TEXT_VALUE"] for item in product_data}

    billing = Billing(
        city=product_data_dict.get("subscriptions[1].billing.city"),
        email=product_data_dict.get("subscriptions[1].billing.email"),
        firstName=product_data_dict.get("subscriptions[1].billing.firstName"),
        fullName=product_data_dict.get("subscriptions[1].billing.fullName"),
        fullStreet=product_data_dict.get("subscriptions[1].billing.fullStreet"),
        houseNo=product_data_dict.get("subscriptions[1].billing.houseNo"),
        invoiceEmailAddress=product_data_dict.get("subscriptions[1].billing.invoiceEmailAddress"),
        invoiceType=product_data_dict.get("subscriptions[1].billing.invoiceType"),
        lastName=product_data_dict.get("subscriptions[1].billing.lastName"),
        street=product_data_dict.get("subscriptions[1].billing.street"),
        zip=product_data_dict.get("subscriptions[1].billing.zip")
    )

    contract = Contract(
        ban=product_data_dict.get("subscriptions[1].contract.ban"),
        existingBan=product_data_dict.get("subscriptions[1].contract.existingBan")
    )

    disclaimers = [
        Disclaimer(text=product_data_dict.get(f"subscriptions[1].disclaimers[{i}].text"))
        for i in range(1, 3)
    ]

    donor_consent = DonorConsent(
        type=product_data_dict.get("subscriptions[1].donorConsent.type"),
        value=product_data_dict.get("subscriptions[1].donorConsent.value"),
        writtenConsentGiven=product_data_dict.get("subscriptions[1].donorConsent.writtenConsentGiven")
    )

    down_payment = DownPayment(
        downPaymentAmountExVat=float(product_data_dict.get("subscriptions[1].downPayment.downPaymentAmountExVat", 0)),
        downPaymentAmountInVat=float(product_data_dict.get("subscriptions[1].downPayment.downPaymentAmountInVat", 0)),
        installmentAmountExVat=float(product_data_dict.get("subscriptions[1].downPayment.installmentAmountExVat", 0)),
        installmentAmountInVat=float(product_data_dict.get("subscriptions[1].downPayment.installmentAmountInVat", 0)),
        lastInstallmentAmountExVat=float(product_data_dict.get("subscriptions[1].downPayment.lastInstallmentAmountExVat", 0)),
        lastInstallmentAmountInVat=float(product_data_dict.get("subscriptions[1].downPayment.lastInstallmentAmountInVat", 0)),
        lastInstallmentIsDifferent=product_data_dict.get("subscriptions[1].downPayment.lastInstallmentIsDifferent") == "true",
        numberOfInstallments=int(product_data_dict.get("subscriptions[1].downPayment.numberOfInstallments", 0))
    )

    legal = Legal(
        birthDate=product_data_dict.get("subscriptions[1].legal.birthDate"),
        city=product_data_dict.get("subscriptions[1].legal.city"),
        contactPhone=product_data_dict.get("subscriptions[1].legal.contactPhone"),
        email=product_data_dict.get("subscriptions[1].legal.email"),
        firstName=product_data_dict.get("subscriptions[1].legal.firstName"),
        floor=product_data_dict.get("subscriptions[1].legal.floor"),
        fullName=product_data_dict.get("subscriptions[1].legal.fullName"),
        fullStreet=product_data_dict.get("subscriptions[1].legal.fullStreet"),
        houseNo=product_data_dict.get("subscriptions[1].legal.houseNo"),
        identificationMethodType=product_data_dict.get("subscriptions[1].legal.identificationMethodType"),
        lastName=product_data_dict.get("subscriptions[1].legal.lastName"),
        room=product_data_dict.get("subscriptions[1].legal.room"),
        street=product_data_dict.get("subscriptions[1].legal.street"),
        zip=product_data_dict.get("subscriptions[1].legal.zip")
    )

    legal_owner = LegalOwner(
        birthDate=product_data_dict.get("subscriptions[1].legalOwner.birthDate"),
        city=product_data_dict.get("subscriptions[1].legalOwner.city"),
        contactPhone=product_data_dict.get("subscriptions[1].legalOwner.contactPhone"),
        email=product_data_dict.get("subscriptions[1].legalOwner.email"),
        firstName=product_data_dict.get("subscriptions[1].legalOwner.firstName"),
        floor=product_data_dict.get("subscriptions[1].legalOwner.floor"),
        fullName=product_data_dict.get("subscriptions[1].legalOwner.fullName"),
        fullStreet=product_data_dict.get("subscriptions[1].legalOwner.fullStreet"),
        houseNo=product_data_dict.get("subscriptions[1].legalOwner.houseNo"),
        lastName=product_data_dict.get("subscriptions[1].legalOwner.lastName"),
        room=product_data_dict.get("subscriptions[1].legalOwner.room"),
        street=product_data_dict.get("subscriptions[1].legalOwner.street"),
        zip=product_data_dict.get("subscriptions[1].legalOwner.zip")
    )

    user = User(
        birthDate=product_data_dict.get("subscriptions[1].user.birthDate"),
        city=product_data_dict.get("subscriptions[1].user.city"),
        contactPhone=product_data_dict.get("subscriptions[1].user.contactPhone"),
        email=product_data_dict.get("subscriptions[1].user.email"),
        fullName=product_data_dict.get("subscriptions[1].user.fullName"),
        fullStreet=product_data_dict.get("subscriptions[1].user.fullStreet"),
        houseNo=product_data_dict.get("subscriptions[1].user.houseNo"),
        street=product_data_dict.get("subscriptions[1].user.street"),
        zip=product_data_dict.get("subscriptions[1].user.zip")
    )

    services_dict = defaultdict(dict)
    for item in product_data:
        key, value = item["NAME"], item["TEXT_VALUE"]
        if "subscriptions[1].services[" in key:
            service_index = int(key.split("services[")[1].split("]")[0])
            attribute_name = key.split(f"services[{service_index}].")[1]
            services_dict[service_index][attribute_name] = value

    services = [
        Service(
            name=service_data.get("name"),
            monthly_charge_in_vat=service_data.get("monthlyCharge.inVat"),
            action=service_data.get("action"),
            customer_relevant=service_data.get("customerRelevant") == "true",
            flexible_switch_is_telia_finance=False,
            insurance_class=None,
            category=service_data.get("category"),
            lifetime_in_months=service_data.get("lifetimeInMonths"),
        )
        for service_data in services_dict.values()
    ]

    switch_dict = {
        key.split("subscriptions[1].switch.")[1]: value
        for key, value in product_data_dict.items()
        if "subscriptions[1].switch." in key
    }

    switch = Switch(
        number_of_installments=switch_dict.get("numberOfInstallments"),
        installment_amount_in_vat=switch_dict.get("installmentAmount.inVat"),
        included_insurance_in_vat=switch_dict.get("includedInsurance.inVat"),
        included_insurance_ex_vat=switch_dict.get("includedInsurance.exVat"),
        model=switch_dict.get("model"),
        imei=switch_dict.get("imei"),
    ) if switch_dict else None

    subscription = Subscription(
           id=product_data_dict.get("subscriptions[1].id"),
           barcode=product_data_dict.get("subscriptions[1].barcode"),
           billing=billing,
           contract=contract,
           disclaimers=disclaimers,
           donorConsent=donor_consent,
           downPayment=down_payment,
           handset=product_data_dict.get("subscriptions[1].handset"),
           handsetPrice=float(product_data_dict.get("subscriptions[1].handsetPrice", 0)),
           handsetPriceExVat=float(product_data_dict.get("subscriptions[1].handsetPriceExVat", 0)),
           icc=product_data_dict.get("subscriptions[1].icc"),
           imei=product_data_dict.get("subscriptions[1].imei"),
           isNewBan=product_data_dict.get("subscriptions[1].isNewBan") == "true",
           isNewSubscription=product_data_dict.get("subscriptions[1].isNewSubscription") == "true",
           isNpTerminationPermitted=product_data_dict.get("subscriptions[1].isNpTerminationPermitted") == "true",
           isPortingSubscription=product_data_dict.get("subscriptions[1].isPortingSubscription") == "true",
           isPreToPost=product_data_dict.get("subscriptions[1].isPreToPost") == "true",
           isPrepaid=product_data_dict.get("subscriptions[1].isPrepaid") == "true",
           isSimCardHandout=product_data_dict.get("subscriptions[1].isSimCardHandout") == "true",
           legal=legal,
           legalOwner=legal_owner,
           msisdn=product_data_dict.get("subscriptions[1].msisdn"),
           npAfterCommitment=product_data_dict.get("subscriptions[1].npAfterCommitment"),
           npContact=product_data_dict.get("subscriptions[1].npContact"),
           npDate=product_data_dict.get("subscriptions[1].npDate"),
           npMsisdn=product_data_dict.get("subscriptions[1].npMsisdn"),
           npOperator=product_data_dict.get("subscriptions[1].npOperator"),
           offeringChangeType=product_data_dict.get("subscriptions[1].offeringChangeType"),
           operation=product_data_dict.get("subscriptions[1].operation"),
           product=ProductDetails(
               current=CurrentProduct(
                   name=product_data_dict.get("subscriptions[1].product.current"),
                   commitmentEnd=product_data_dict.get("subscriptions[1].product.current.commitmentEnd"),
                   commitmentStart=product_data_dict.get("subscriptions[1].product.current.commitmentStart"),
                   disclaimers=[
                       Disclaimer(text=product_data_dict.get(f"subscriptions[1].product.current.disclaimers[{i}].text"))
                       for i in range(1, 3)
                   ],
                   hasActiveCommitment=product_data_dict.get("subscriptions[1].product.current.hasActiveCommitment") == "true",
                   monthlyCharge=MonthlyCharge(
                       exVat=float(product_data_dict.get("subscriptions[1].product.current.monthlyCharge.exVat", 0)),
                       inVat=float(product_data_dict.get("subscriptions[1].product.current.monthlyCharge.inVat", 0))
                   ),
                   offeringDescriptionLong=product_data_dict.get("subscriptions[1].product.current.offeringDescriptionLong"),
                   offeringDescriptionShort=product_data_dict.get("subscriptions[1].product.current.offeringDescriptionShort"),
                   shortName=product_data_dict.get("subscriptions[1].product.current.shortName")
               ),
               disclaimers=[
                   Disclaimer(text=product_data_dict.get(f"subscriptions[1].product.disclaimers[{i}].text"))
                   for i in range(1, 3)
               ],
               monthlyCharge=MonthlyCharge(
                   exVat=float(product_data_dict.get("subscriptions[1].product.monthlyCharge.exVat", 0)),
                   inVat=float(product_data_dict.get("subscriptions[1].product.monthlyCharge.inVat", 0))
               ),
               offeringDescriptionLong=product_data_dict.get("subscriptions[1].product.offeringDescriptionLong"),
               offeringDescriptionShort=product_data_dict.get("subscriptions[1].product.offeringDescriptionShort"),
               shortName=product_data_dict.get("subscriptions[1].product.shortName")
           ),
           resultingServices=product_data_dict.get("subscriptions[1].resultingServices", "").split(","),
           services=services,
           simType=product_data_dict.get("subscriptions[1].simType"),
           user=user
    )

    return subscription