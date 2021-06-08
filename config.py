db = {
    'user'     : 'quaterteam',
    'password' : 'quater',
    'host'     : 'team02.kitcomputer.kr',
    'port'     : '5102',
    'database' : 'wedb'
}

DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8" 