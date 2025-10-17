import json

class RestAPI:
    def __init__(self, database=None):
        self.database = self.index_database(database)
        pass

    def restore_database(self, data):
        return {'users': [data[user] for user in data]}
        
    def index_database(self, data):
        return {user['name']: user for user in data['users']}
        
                
    def get(self, url, payload=None):
        return json.dumps({'users' : [self.database[user] for user in json.loads(payload)['users']] if payload else []})
        
    def post(self, url, payload=None):
        payload = json.loads(payload)
        if url == '/add':
            return json.dumps(self.create_user(payload))
        elif url == '/iou':
            return json.dumps(self.create_iou(payload))
            

    def create_user(self, user_to_add):
        data_format = {'name': user_to_add['user'], 'owes': {}, 'owed_by': {}, 'balance': 0.0}
        self.database[user_to_add['user']] = data_format
        return data_format

    def create_iou(self, iou):
        # comprobamos si hay deuda
        if iou['borrower'] in self.database[iou['lender']]['owes']:
            if self.database[iou['lender']]['owes'][iou['borrower']] <= iou["amount"]:
                # Agregamos deuda
                iou['amount'] -= self.database[iou['lender']]['owes'][iou['borrower']]
                self.database[iou['lender']]['balance'] += self.database[iou['lender']]['owes'][iou['borrower']]
                self.database[iou['borrower']]['balance'] -= self.database[iou['borrower']]['owed_by'][iou['lender']]
                del self.database[iou['lender']]['owes'][iou['borrower']]
                del self.database[iou['borrower']]['owed_by'][iou['lender']]
                #iou['lender'], iou['borrower'] = iou['borrower'],iou['lender']
                if iou['amount'] > 0:
                    self.create_iou(iou)
            else:
                # Agregamos deuda
                self.database[iou['lender']]['owes'][iou['borrower']] -= iou['amount']
                self.database[iou['lender']]['balance'] += iou['amount']
                # Agregamos prestamo
                self.database[iou['borrower']]['owed_by'][iou['lender']] -= iou['amount']
                self.database[iou['borrower']]['balance'] -= iou['amount']
                print(self.database)
        else:
            # Agregamos deuda
            self.database[iou['lender']]['owed_by'][iou['borrower']] = iou['amount']
            self.database[iou['lender']]['balance'] += iou['amount']
            # Agregamos prestamo
            self.database[iou['borrower']]['owes'][iou['lender']] = iou['amount']
            self.database[iou['borrower']]['balance'] -= iou['amount']

        print(self.database)
        return ({'users': sorted([self.database[iou['lender']], self.database[iou['borrower']]], key=lambda user: user["name"])
                 })
