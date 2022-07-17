from ctypes import addressof
import email
from http import client
import streamlit as st
from datetime import datetime, date
from pyinvoice.models import InvoiceInfo, ServiceProviderInfo, ClientInfo, Item, Transaction
from pyinvoice.templates import SimpleInvoice




doc = SimpleInvoice('.pdf')
download=st.button("Download")
if download:
    doc = SimpleInvoice('.pdf')

# Paid stamp, optional
doc.is_paid = False

doc.invoice_info = InvoiceInfo(datetime.now())  # Invoice info, optional

right_column, left_column =st.columns(2)
#From Company
with right_column:
    invoice_num =st.text_input("Invoice Number")
    from_compmany =st.text_input("Company Name")
    street =st.text_input(f"Street and Cross")
    city=st.text_input("Area & City")
    state_country=st.text_input("Enter State & Country")
    pin_code=st.text_input("Area Pin Code")

doc.invoice_info = InvoiceInfo(invoice_num)

#To Company
with left_column:
    clientid=st.text_input("Client ID")
    to_company =st.text_input("Bill To")
    to_street =st.text_input(f"Street and Cross ")
    to_city=st.text_input("Area & City ")
    to_state_country=st.text_input("Enter State & Country ")
    to_pin_code=st.text_input("Area Pin Code ")


# Service Provider Info, optional
doc.service_provider_info = ServiceProviderInfo(
    name= from_compmany,
    street= street,
    city= city,
    state= state_country,
    post_code= pin_code,
    
)

# Client info, optional
doc.client_info = ClientInfo(
    client_id=clientid,
    name=to_company,
    street=to_street,
    city=to_city,
    state=to_state_country,
    post_code=to_pin_code,
    )

st.markdown("---")
col1,col2,col3,col4 =st.columns(4)
with col1:
    item1=st.text_input("Category")
    item2=st.text_input(" ")
    item3=st.text_input("  ")
    item4=st.text_input("   ")
    item5=st.text_input("    ")
with col2:
    itemdes1=st.text_input("item Description")
    itemdes2=st.text_input("")
    itemdes3=st.text_input("       ")
    itemdes4=st.text_input("             ")
    itemdes5=st.text_input("            ")

with col3:
    qty1=int(float(st.number_input("Qty / units")))
    qty2=int(float(st.number_input("                     ")))
    qty3=int(float(st.number_input("                       ")))
    qty4=int(float(st.number_input("                         ")))
    qty5=int(float(st.number_input("                           ")))

with col4:
    rate1=int(float(st.number_input("Rate")))
    rate2=int(float(st.number_input("                                   ")))
    rate3=int(float(st.number_input("                                     ")))
    rate4=int(float(st.number_input("                                        ")))
    rate5=int(float(st.number_input("                                          ")))

# Add Item
doc.add_item(Item(item1, itemdes1, qty1, rate1))
doc.add_item(Item(item2, itemdes2, qty2, rate2))
doc.add_item(Item(item3, itemdes3, qty3, rate3))
doc.add_item(Item(item4, itemdes4, qty4, rate4))
doc.add_item(Item(item5, itemdes5, qty5, rate5))

st.markdown("---")
tax=st.selectbox('GST',
    ('0','5','12','18'))
# Tax rate, optional
doc.set_item_tax_rate(tax)  # 20%

# Transactions detail, optional
#doc.add_transaction(Transaction('Paypal', 111, datetime.now(), 1))
#doc.add_transaction(Transaction('Stripe', 222, date.today(), 2))

# Optional
doc.set_bottom_tip("Email: example@example.com<br />Don't hesitate to contact us for any questions.")


doc.finish()