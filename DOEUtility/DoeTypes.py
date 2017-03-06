def CreateRows(self,dom):
    parent = dom.createElement("Grid.RowDefinitions")
    child = dom.createElement("RowDefinition")
    child.setAttribute('Height', 'Auto')
    parent.appendChild(child)
    return parent

def CreateColumns(self,dom,currWidth):
    parent = dom.createElement("Grid.ColumnDefinitions")
    child = dom.createElement("ColumnDefinition")
    child.setAttribute('Width', currWidth)
    parent.appendChild(child)
    return parent

def TextBlock(self,dom,param,row,col):
    parent = dom.createElement("TextBlock")
    parent.setAttribute('Grid.Row', str(row))
    parent.setAttribute('Grid.Column', str(col))
    parent.setAttribute('x:Name', "lbl{}".format(param.replace(" ","")))
    parent.setAttribute('Style', "{StaticResource TextBlockStyle}")
    parent.setAttribute('Text', "{}:".format(param))
    return parent

def DateTime(self,dom,param,row,col,attributeName):
    binding = "Binding ExternalAlgoProperties[(i:Description){}-{}, ValidatesOnDataErrors=True, ValidatesOnExceptions=True".format(attributeName,param.replace(" ",""))
    parent = dom.createElement("i:DateTimePicker")
    parent.setAttribute('Grid.Row', str(row))
    parent.setAttribute('Grid.Column', str(col))
    parent.setAttribute('x:Name', param.replace(" ",""))
    parent.setAttribute('Style', "{StaticResource TextBlockStyle}")
    parent.setAttribute('Focusable', "False")
    parent.setAttribute('IsDatePicker', "False")
    parent.setAttribute('IsTimePicker', "True")
    parent.setAttribute('SelectedDateTime', "{" + binding + "}")
    return parent