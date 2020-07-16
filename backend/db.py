import psycopg2
from psycopg2.extras import DictCursor


class DB:
    cursor = None
    connection = None
    schema = 'main'

    def __init__(self, dbname, user, password, host):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host

    def connect(self):
        self.connection = psycopg2.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host)

        self.cursor = self.connection.cursor(cursor_factory=DictCursor)

    def get_all_from_table(self, table_name):
        self.cursor.execute(f"SELECT * FROM {self.schema}.{table_name}")
        records = self.cursor.fetchall()
        return records

    def get_id_by_name(self, table_name, element_name):
        self.cursor.execute(f"SELECT id FROM {self.schema}.{table_name} WHERE name='{element_name}'")
        record = self.cursor.fetchone()[0]
        return record

    def get_buttons_name(self):
        self.cursor.execute(f"SELECT name FROM {self.schema}.buttons")
        records = self.cursor.fetchall()
        flattened = [val for sublist in records for val in sublist]
        return flattened

    def get_name_by_slug(self, slug):
        self.cursor.execute(f"SELECT name FROM {self.schema}.buttons WHERE slug='{slug}'")
        record = self.cursor.fetchone()[0]
        return record

    def insert_data_to_phrases(self, values):
        try:
            query = f"INSERT INTO {self.schema}.phrase (button_id, user_n, text, created_at, lang) " \
                    f"VALUES(%s, %s, %s, %s, %s)"
            self.cursor.execute(
                query, values
            )
            self.connection.commit()
            return 'Inserted Successfully!'
        except (Exception, psycopg2.Error) as error:
            return error

    def get_all_phrases(self):
        dt = []
        result = {}
        self.cursor.execute(
            f"""
            SELECT 
                {self.schema}.phrase.user_n,
                {self.schema}.phrase.lang,
                {self.schema}.buttons.name, 
                {self.schema}.buttons.slug,
                {self.schema}.phrase.text
            FROM {self.schema}.phrase 
                JOIN {self.schema}.buttons ON {self.schema}.buttons.id = {self.schema}.phrase.button_id 
            """
        )

        for record in self.cursor.fetchall():
            dt.append(
                {
                    record[0]: {
                        record[1]: {
                            record[3]: record[4]
                        }
                    }
                }
            )

        for key, value in self._list_to_dict_phrases(dt).items():
            result[key] = self._list_to_dict_phrases(value)

        for key1, value1 in result.items():
            for key2, value2 in value1.items():
                result[key1][key2] = self._list_to_dict_phrases(value2)

        return result

    @staticmethod
    def _list_to_dict_phrases(dt):
        temp = {}
        for dic in dt:
            for key in (temp.keys() | dic.keys()):
                if key in dic:
                    temp.setdefault(key, []).append(dic[key])

        return temp

    def get_phrases_by_user_and_lang(self, user, lang):
        dt = []
        self.cursor.execute(
            f"""
                SELECT 
                    {self.schema}.buttons.slug,
                    {self.schema}.phrase.text
                FROM {self.schema}.phrase
                        JOIN {self.schema}.buttons ON {self.schema}.buttons.id = {self.schema}.phrase.button_id
                WHERE {self.schema}.phrase.user_n = '{user}' AND {self.schema}.phrase.lang = '{lang}'
            """
        )

        for record in self.cursor.fetchall():
            dt.append(
                {
                    record[0]: record[1]
                }
            )

        return self._list_to_dict_phrases(dt)

    def get_phrases_by_lang(self, lang):
        dt = []
        self.cursor.execute(
            f"""
                SELECT 
                    {self.schema}.buttons.slug,
                    {self.schema}.phrase.text
                FROM {self.schema}.phrase
                        JOIN {self.schema}.buttons ON {self.schema}.buttons.id = {self.schema}.phrase.button_id
                WHERE {self.schema}.phrase.lang = '{lang}'
            """
        )

        for record in self.cursor.fetchall():
            dt.append(
                {
                    record[0]: record[1]
                }
            )

        return self._list_to_dict_phrases(dt)

    def __del__(self):
        self.cursor.close()
        self.connection.close()

# # print(
# #     db.insert_data_to_phrases(
# #         (1, 1, 'test', datetime.date.today(), db.get_id_by_name('lang', 'ua'))
# #     )
# # )
# # print(db.get_all_from_table('phrase'))
# # pprint(db.get_all_phrases())
# data = db.get_all_phrases()
# # print(db.get_all_from_table_by_custom_field('phrase', 'lang_id', 2))
# print(db.get_phrases_by_user_and_lang('Vasya', 'ua'))
# print(db.get_phrases_by_lang('ru'))
# pprint(data)
