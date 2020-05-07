# Parse XML content column on CSV file

Given a CSV file with XML content column, this task gets the value of it by locale.

I use it, for example, to get value of XML content on Liferay database tables (version CE 6.1).

```xml
<?xml version='1.0' encoding='UTF-8'?><root available-locales="ca_ES,es_ES,en_GB," default-locale="ca_ES"><Name languageid="ca_ES">Voluptua</Name><Name languageid="es_ES">Dolores</Name><Name languageid="en_GB">Et</Name></root>
```

If locale doesn't exist, it takes the 'default-locale'. For example, if you want 'en_GB' name and it doesn't exist, the task will return 'ca_ES' name.

## Arguments

| Parameter         | Type    | Description                | Required | Default value    |
|-------------------|---------|----------------------------|----------|------------------|
| --help (or -h)    |         | Show help message and exit |          |                  |
| --inputfile       | String  | Input file name.           | True     |                  |
| --outputfile      | Stirng  | Output file name.          | True     |                  |
| --column          | Integer | Column number.             | False    | 0 (first column) |
| --locale          | String  | Locale key.                | False    | ca_ES (catalan)  |
| --ignoreheaderrow |         | Ignore first row (header). | False    |                  |

## Example

### Call

> py main.py --inputfile example/pages_sorted.csv --column 3 --ignoreheaderrow

### Input file example (see /example/pages.csv)

| plid    | layoutId | parentLayoutId | name                                                                                                                                                                                                                                    | priority |
|---------|----------|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| 7004446 | 74       | 1              | `<?xml version='1.0' encoding='UTF-8'?><root available-locales="ca_ES,es_ES,en_GB," default-locale="ca_ES"><Name languageid="ca_ES">Invidunt</Name><Name languageid="es_ES">Diam</Name><Name languageid="en_GB">Voluptua</Name></root>` | 15       |
| 8152170 | 205      | 1              | `<?xml version='1.0' encoding='UTF-8'?><root available-locales="ca_ES" default-locale="ca_ES"><Name languageid="ca_ES">Labore</Name></root>`                                                                                            | 10       |
| 6724205 | 1        | 0              | `<?xml version='1.0' encoding='UTF-8'?><root available-locales="ca_ES,es_ES,en_GB," default-locale="ca_ES"><Name languageid="ca_ES">Diam</Name><Name languageid="es_ES">Magna</Name><Name languageid="en_GB">Aliquyam</Name></root>`    | 0        |
| 8152195 | 206      | 205            | `<?xml version='1.0' encoding='UTF-8'?><root available-locales="ca_ES,es_ES" default-locale="ca_ES"><Name languageid="ca_ES">Nonumy</Name><Name languageid="es_ES">Aliquyam</Name></root>`                                              | 0        |
| 8220383 | 222      | 205            | `<?xml version='1.0' encoding='UTF-8'?><root available-locales="ca_ES,es_ES,en_GB," default-locale="ca_ES"><Name languageid="ca_ES">Consetetur</Name><Name languageid="es_ES">Ut</Name><Name languageid="en_GB">Labore</Name></root>`   | 1        |

### Output file

| plid    | layoutId | parentLayoutId | name       | priority |
|---------|----------|----------------|------------|----------|
| 7004446 | 74       | 1              | Invidunt   | 15       |
| 8152170 | 205      | 1              | Labore     | 10       |
| 6724205 | 1        | 0              | Diam       | 0        |
| 8152195 | 206      | 205            | Nonumy     | 0        |
| 8220383 | 222      | 205            | Consetetur | 1        |

## Improvements

- Add possibility to indicate CSV delimiter by call parameter.
