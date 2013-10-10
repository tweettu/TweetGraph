import pingdom

connection = pingdom.PingdomConnection('it.info@sportclips.com', 'Sc00byD00')
connection.apikey = "nog1os9rtnzbr59t18a8q93a68xlwas4"

checks = connection.get_all_checks()

req = pingdom.PingdomRequest(connnection, )


exit()

for check in checks:
    checkdetails = connection.get_check(check.id)
    contactids = checkdetails.contactids
    print checkdetails.name #, checkdetails.contactids
    for contactid in contactids:
        print contactid
        # req = pingdom.PingdomRequest(connection=connection,
        #                              resource='/get/resource')
        # contactlist = {"contactid": contactid}
        # contact2 = pingdom.PingdomContact(contactlist)

        # property_names = [p for p in dir(contact2) if isinstance(getattr(
        #     contact2, p), property)]
        # print contact2.__str__()
        # contact = pingdom.PingdomContact(contactid)
        # print contact.name

