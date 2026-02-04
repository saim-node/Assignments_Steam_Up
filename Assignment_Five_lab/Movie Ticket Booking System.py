ticket_ids = ["AVT1215M", "TLR0818E", "HPT1012A"]
group_price = 0

def extract_ticket_details(ticket_ids):
    tickets = []
    for t in ticket_ids:
        ticket = {
            "Movie Code": t[:3],
            "Seat Number": t[3:5],
            "Ticket Price": int(t[5:7]),
            "Show Time": t[7]
        }
        tickets.append(ticket)
    return tickets

result = extract_ticket_details(ticket_ids)

for ticket in result:
    print(f"""
Movie Code    : {ticket['Movie Code']}
Seat Number   : {ticket['Seat Number']}
Ticket Price  : ${ticket['Ticket Price']}
Show Time     : {ticket['Show Time']}
""")
    
    group_price += ticket['Ticket Price']

print("The total group price is $", group_price)
