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

def TextBlock(self,dom,param,row,col,isMandaory=False):
    parent = dom.createElement("TextBlock")
    parent.setAttribute('Grid.Row', str(row))
    parent.setAttribute('Grid.Column', str(col))
    parent.setAttribute('x:Name', "lbl{}".format(param.replace(" ","")))
    parent.setAttribute('Style', "{StaticResource TextBlockStyle}")
    parent.setAttribute('Text', "{}:".format(param))
    return parent

def DateTime(self,dom,param,row,col,attributeName,isMandaory):
    binding = "Binding Path=ExternalAlgoProperties[(i:Description){}-{}].Value, ValidatesOnDataErrors=True, ValidatesOnExceptions=True".format(attributeName,param.replace(" ",""))
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

def ComboBox(self,dom,param,row,col,attributeName,isMandatory):
    binding = ""
    if eval(isMandatory):
        binding = "ExternalAlgoProperties[(i:Description){}-{}].Value".format(attributeName,param.replace(" ",""))
    else:
        binding = "Binding Path=ExternalAlgoProperties[(i:Description){}-{}].AvailableItems, ValidatesOnDataErrors=True, ValidatesOnExceptions=True".format(attributeName,param.replace(" ",""))
       
    enabled = "Binding Path=ExternalAlgoProperties[(i:Description){}-{}].IsEditable".format(attributeName,param.replace(" ",""))
    parent = dom.createElement("i:ComboBox")
    parent.setAttribute('Grid.Row', str(row))
    parent.setAttribute('Grid.Column', str(col))
    parent.setAttribute('x:Name', param.replace(" ",""))
    parent.setAttribute('Style', "{StaticResource TextBlockStyle}")
    parent.setAttribute('IsSorted', "False")
    parent.setAttribute('IsEditable', "False")
    parent.setAttribute('CloseDropDownOnTab', "True")
    parent.setAttribute('ItemsSource', "{" + binding + "}")
    if eval(isMandatory):
        child = dom.createElement("i:ComboBox.SelectedItem")
        firstChild = dom.createElement("Binding")
        firstChild.setAttribute('Path', binding)
        firstChild.setAttribute('ValidatesOnDataErrors', 'True')
        firstChild.setAttribute('ValidatesOnExceptions', 'True')
        firstChild.setAttribute('UpdateSourceTrigger', 'PropertyChanged')
        child.appendChild(firstChild)
        secondChild = dom.createElement("Binding.ValidationRules")
        firstChild.appendChild(secondChild)
        thirdChild = dom.createElement("i:ValueEmptyValidationRule")
        thirdChild.setAttribute('ElementId', param.replace(" ",""))
        thirdChild.setAttribute('ValidatesOnTargetUpdated', 'True')
        secondChild.appendChild(thirdChild)
        parent.appendChild(child)

    return parent