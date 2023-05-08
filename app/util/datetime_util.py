from dateutil import parser


def get_date_object(string):
    return parser.parse(string).date()
