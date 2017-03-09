def CreateRows(self,dom,parent):
    child = dom.createElement("RowDefinition")
    child.setAttribute('Height', 'Auto')
    parent.appendChild(child)
    return parent

def CreateColumns(self,dom,parent,currWidth):
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
    parent.setAttribute('Style', "{StaticResource BasicStyle}")
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
       
    editable = "Binding Path=ExternalAlgoProperties[(i:Description){}-{}].IsEditable".format(attributeName,param.replace(" ",""))
    parent = dom.createElement("i:ComboBox")
    parent.setAttribute('Grid.Row', str(row))
    parent.setAttribute('Grid.Column', str(col))
    parent.setAttribute('x:Name', param.replace(" ",""))
    parent.setAttribute('Style', "{StaticResource BasicStyle}")
    parent.setAttribute('IsSorted', "False")
    parent.setAttribute('IsEditable', "False")
    parent.setAttribute('CloseDropDownOnTab', "True")
    parent.setAttribute('ItemsSource', "{" + binding + "}")
    parent.setAttribute('IsEnabled', "{" + editable + "}")
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

def NumericUpDown(self,dom,param,row,col,attributeName,isMandatory):
    binding = "Binding Path=ExternalAlgoProperties[(i:Description){}-{}].Value, ValidatesOnDataErrors=True, ValidatesOnExceptions=True".format(attributeName,param.replace(" ",""))
    editable = "Binding Path=ExternalAlgoProperties[(i:Description){}-{}].IsEditable".format(attributeName,param.replace(" ",""))
    parent = dom.createElement("i:NumericUpDown")
    parent.setAttribute('Grid.Row', str(row))
    parent.setAttribute('Grid.Column', str(col))
    parent.setAttribute('x:Name', param.replace(" ",""))
    parent.setAttribute('Style', "{StaticResource BasicStyle}")
    parent.setAttribute('DisplayFormat', "0")
    parent.setAttribute('RoundingDecimalPlaces', "0")
    parent.setAttribute('Minimum', "1")
    parent.setAttribute('Maximum', "100")
    parent.setAttribute('Increment', "1")
    parent.setAttribute('IncrementCount', "1")
    parent.setAttribute('Value', "{" + binding + "}")
    parent.setAttribute('IsEnabled', "{" + editable + "}")
    return parent

def CheckBox(self,dom,param,row,col,attributeName,isMandatory):
    binding = "Binding Path=ExternalAlgoProperties[(i:Description){}-{}].Value, ValidatesOnDataErrors=True, ValidatesOnExceptions=True".format(attributeName,param.replace(" ",""))
    editable = "Binding Path=ExternalAlgoProperties[(i:Description){}-{}].IsEditable".format(attributeName,param.replace(" ",""))
    parent = dom.createElement("CheckBox")
    parent.setAttribute('Grid.Row', str(row))
    parent.setAttribute('Grid.Column', str(col))
    parent.setAttribute('x:Name', param.replace(" ",""))
    parent.setAttribute('Style', "{StaticResource BasicStyle}")
    parent.setAttribute('IsChecked', "{" + binding + "}")
    parent.setAttribute('IsEnabled', "{" + editable + "}")
    return parent