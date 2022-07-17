from ctypes import addressof
import email
from http import client
import streamlit as st
from datetime import datetime, date
from pyinvoice.models import InvoiceInfo, ServiceProviderInfo, ClientInfo, Item, Transaction
from pyinvoice.templates import SimpleInvoice
from fpdf import FPDF
import base64
import requests

st.set_page_config(page_title="Invoice Tool",page_icon=":page_facing_up:",layout="centered")
st.header("Invoice Genrator:page_facing_up:")

with open(".pdf","rb")as pdf_file:
        PDFbyte = pdf_file.read()
save=st.button('Save')
if save:
    st.success("Click Export to Download Invoice")
    st.download_button(label="Export_Report",
                    data=PDFbyte,
                    file_name=f"Invoice.pdf",
                    mime='application/octet-stream')

doc = SimpleInvoice('.pdf')
#download=st.button("Download")
#if download:
    #doc = SimpleInvoice('.pdf')

# Paid stamp, optional
doc.is_paid = False

doc.invoice_info = InvoiceInfo(datetime.now(),datetime.now())  # Invoice info, optional

right_column, left_column, other_col =st.columns(3)
#From Company
with right_column:
    invoice_num =st.text_input("Invoice Number")
    from_compmany =st.text_input("Company Name")
    street =st.text_input(f"Street and Cross")
    city=st.text_input("Area & City")
    state_country=st.text_input("Enter State & Country")
    pin_code=st.text_input("Area Pin Code")

doc.invoice_info = InvoiceInfo(invoice_num,datetime.now())

#To Company
with left_column:
    clientid=st.text_input("Client ID")
    to_company =st.text_input("Bill To")
    to_street =st.text_input(f"Street and Cross ")
    to_city=st.text_input("Area & City ")
    to_state_country=st.text_input("Enter State & Country ")
    to_pin_code=st.text_input("Area Pin Code ")

with other_col:
    phone=st.text_input("Enter Contact Number")
    tax=st.selectbox('GST',
    ('0','5','12','18'))
    st.warning(f"Please Note this program does not capture your data/information, the data you enter directly downloads to PDF format. This Tool is purely written in Python and help local vendor who find difficulties to genrate Invoice")

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
st.subheader("Add Item/Service Description")
col1,col2,col3,col4 =st.columns(4)
with col1:
    item1=st.text_input("Category")
    item2=st.text_input(" ")
    item3=st.text_input("  ")
    item4=st.text_input("   ")
    item5=st.text_input("    ")
    item6=st.text_input("     ")
with col2:
    itemdes1=st.text_input("item Description")
    itemdes2=st.text_input("")
    itemdes3=st.text_input("       ")
    itemdes4=st.text_input("             ")
    itemdes5=st.text_input("            ")
    itemdes6=st.text_input("               ")

with col3:
    qty1=int(float(st.number_input("Qty / units",min_value=0)))
    qty2=int(float(st.number_input("                     ",min_value=0)))
    qty3=int(float(st.number_input("                       ",min_value=0)))
    qty4=int(float(st.number_input("                         ",min_value=0)))
    qty5=int(float(st.number_input("                           ",min_value=0)))
    qty6=int(float(st.number_input("                            ",min_value=0)))

with col4:
    rate1=int(float(st.number_input("Rate",min_value=0)))
    rate2=int(float(st.number_input("                                   ",min_value=0)))
    rate3=int(float(st.number_input("                                     ",min_value=0)))
    rate4=int(float(st.number_input("                                        ",min_value=0)))
    rate5=int(float(st.number_input("                                          ",min_value=0)))
    rate6=int(float(st.number_input("                                           ",min_value=0)))

# Add Item
doc.add_item(Item(item1, itemdes1, qty1, rate1))
doc.add_item(Item(item2, itemdes2, qty2, rate2))
doc.add_item(Item(item3, itemdes3, qty3, rate3))
doc.add_item(Item(item4, itemdes4, qty4, rate4))
doc.add_item(Item(item5, itemdes5, qty5, rate5))
doc.add_item(Item(item6, itemdes6, qty6, rate6))

# Tax rate, optional
doc.set_item_tax_rate(tax)  # 20%
# Transactions detail, optional
#doc.add_transaction(Transaction('Paypal', 111, datetime.now(), 1))
#doc.add_transaction(Transaction('Stripe', 222, date.today(), 2))

# Optional
doc.set_bottom_tip(f"Contact:{phone} <br />This is computer generated Invoice does not require seal and signature")
st.markdown("---")
st.text("Get In touch with me for any related query at shiazasif.data@gmail.com")   
doc.finish()