class RowForOffering:
    def __init__(self, offRowText, offRowValue, offRowIsAdditionalText):
        self.offRowText = offRowText
        self.offRowValue = offRowValue
        self.offRowIsAdditionalText = offRowIsAdditionalText

    def __repr__(self):
        return f"text='{self.offRowText}', value='{self.offRowValue}'"

    def toTableRow(self):
        return f"| {self.offRowText:<50} | {self.offRowValue:<20} |"

def printTable(rows):
    header = f"| {'Text':<50} | {'Value':<20} |"
    separator = f"+{'-'*52}+{'-'*22}+"
    print(separator)
    print(header)
    print(separator)
    for row in rows:
        print(row.toTableRow())
    print(separator)