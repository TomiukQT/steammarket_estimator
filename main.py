import steammarket as sm
import prices_parser as parser

CSGO_ID = 730
TEST_ITEM = 'AK-47 | Redline (Field-Tested)'


def main():
    item_info = sm.get_item(CSGO_ID, TEST_ITEM)
    print(item_info)
    item_history = sm.get_item_history(CSGO_ID, TEST_ITEM)
    df = parser.parse_item_history(item_history)
    df = df.astype({
        'date': 'datetime64',
        'amount': 'int64',
    })
    print(df.info())


if __name__ == '__main__':
    main()
