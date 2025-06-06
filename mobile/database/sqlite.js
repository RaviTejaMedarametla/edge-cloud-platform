import * as SQLite from 'expo-sqlite';

const db = SQLite.openDatabase('app.db');

export function init() {
  return new Promise((resolve, reject) => {
    db.transaction(tx => {
      tx.executeSql(
        'CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY NOT NULL, value TEXT NOT NULL);',
        [],
        () => resolve(),
        (_, err) => reject(err)
      );
    });
  });
}

export default db;
