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

def TextBlock(self,dom,param,row,col,attributeName,isMandaory,minimum,maximum,increment,rounding,displayformat,visibility):
    pName = param
    binding = "Binding Path=ExternalAlgoProperties[(i:Description){}-{}].Value".format(attributeName,param.replace("%","Percent").replace(" ",""))
    parent = dom.createElement("TextBlock")
    parent.setAttribute('Grid.Row', str(row))
    parent.setAttribute('Grid.Column', str(col))
    parent.setAttribute('x:Name', "Lbl{}".format(param.replace("%","Percent").replace(" ","")))
    parent.setAttribute('Style', "{StaticResource TextBlockStyle}")
    if visibility != "Visible":
        parent.setAttribute('Visibility',visibility)
        parent.setAttribute('Text', "{" + binding + "}")
    else:
        parent.setAttribute('Text', "{}:".format(pName))
    return parent

def DateTime(self,dom,param,row,col,attributeName,isMandaory,minimum,maximum,increment,rounding,displayformat,visibility):
    pName = param.replace("%","Percent").replace(" ","")
    binding = "Binding Path=ExternalAlgoProperties[(i:Description){}-{}].Value, ValidatesOnDataErrors=True, ValidatesOnExceptions=True".format(attributeName,pName)
    editable = "Binding Path=ExternalAlgoProperties[(i:Description){}-{}].IsEditable".format(attributeName,pName)
    parent = dom.createElement("i:DateTimePicker")
    parent.setAttribute('Grid.Row', str(row))
    parent.setAttribute('Grid.Column', str(col))
    parent.setAttribute('x:Name', pName)
    parent.setAttribute('Style', "{StaticResource BasicStyle}")
    parent.setAttribute('Focusable', "False")
    parent.setAttribute('IsDatePicker', "False")
    parent.setAttribute('IsTimePicker', "True")
    parent.setAttribute('SelectedDateTime', "{" + binding + "}")
    parent.setAttribute('IsEnabled', "{" + editable + "}")
    if visibility != "Visible":
        parent.setAttribute('Visibility',visibility)
    return parent

def ComboBox(self,dom,param,row,col,attributeName,isMandatory,minimum,maximum,increment,rounding,displayformat,visibility):
    pName = param.replace("%","Percent").replace(" ","")
    binding = ""
    if eval(isMandatory):
        binding = "ExternalAlgoProperties[(i:Description){}-{}].Value".format(attributeName,pName)
    
    itemSource = "Binding Path=ExternalAlgoProperties[(i:Description){}-{}].AvailableItems, ValidatesOnDataErrors=True, ValidatesOnExceptions=True".format(attributeName,pName)
       
    editable = "Binding Path=ExternalAlgoProperties[(i:Description){}-{}].IsEditable".format(attributeName,pName)
    parent = dom.createElement("i:ComboBox")
    parent.setAttribute('Grid.Row', str(row))
    parent.setAttribute('Grid.Column', str(col))
    parent.setAttribute('x:Name', pName)
    parent.setAttribute('Style', "{StaticResource BasicStyle}")
    parent.setAttribute('IsSorted', "False")
    parent.setAttribute('IsEditable', "False")
    parent.setAttribute('CloseDropDownOnTab', "True")
    parent.setAttribute('ItemsSource', "{" + itemSource + "}")
    parent.setAttribute('IsEnabled', "{" + editable + "}")
    if visibility != "Visible":
        parent.setAttribute('Visibility',visibility)
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
        thirdChild.setAttribute('ElementId', pName)
        thirdChild.setAttribute('ValidatesOnTargetUpdated', 'True')
        secondChild.appendChild(thirdChild)
        parent.appendChild(child)

    return parent

# minimum and maximum values are not mandtory in csv, if their values are "1"
# and "100" respectively
def NumericUpDown(self,dom,param,row,col,attributeName,isMandatory,minimum,maximum,increment,rounding,displayformat,visibility):
    pName = param.replace("%","Percent").replace(" ","")
    binding = "Binding Path=ExternalAlgoProperties[(i:Description){}-{}].Value, ValidatesOnDataErrors=True, ValidatesOnExceptions=True".format(attributeName,pName)
    editable = "Binding Path=ExternalAlgoProperties[(i:Description){}-{}].IsEditable".format(attributeName,pName)
    parent = dom.createElement("i:NumericUpDown")
    parent.setAttribute('Grid.Row', str(row))
    parent.setAttribute('Grid.Column', str(col))
    parent.setAttribute('x:Name', pName)
    parent.setAttribute('Style', "{StaticResource BasicStyle}")
    parent.setAttribute('DisplayFormat', "0" if displayformat is None or "" else displayformat)
    parent.setAttribute('RoundingDecimalPlaces', "0" if rounding is None or "" else rounding)
    parent.setAttribute('Minimum', "1" if minimum is None or "" else minimum)
    parent.setAttribute('Maximum', "100" if maximum is None or "" else maximum)
    parent.setAttribute('Increment', "1" if increment is None or "" else increment)
    parent.setAttribute('IncrementCount', "1")
    parent.setAttribute('Value', "{" + binding + "}")
    parent.setAttribute('IsEnabled', "{" + editable + "}")
    if visibility != "Visible":
        parent.setAttribute('Visibility',visibility)
    return parent

def CheckBox(self,dom,param,row,col,attributeName,isMandatory,minimum,maximum,increment,rounding,displayformat,visibility):
    pName = param.replace("%","Percent").replace(" ","")
    binding = "Binding Path=ExternalAlgoProperties[(i:Description){}-{}].Value, ValidatesOnDataErrors=True, ValidatesOnExceptions=True".format(attributeName,pName)
    editable = "Binding Path=ExternalAlgoProperties[(i:Description){}-{}].IsEditable".format(attributeName,pName)
    parent = dom.createElement("CheckBox")
    parent.setAttribute('Grid.Row', str(row))
    parent.setAttribute('Grid.Column', str(col))
    parent.setAttribute('x:Name', pName)
    parent.setAttribute('Style', "{StaticResource BasicStyle}")
    parent.setAttribute('IsChecked', "{" + binding + "}")
    parent.setAttribute('IsEnabled', "{" + editable + "}")
    if visibility != "Visible":
        parent.setAttribute('Visibility',visibility)
    return parent

def TextBox(self,dom,param,row,col,attributeName,isMandatory,minimum,maximum,increment,rounding,displayformat,visibility):
    pName = param.replace("%","Percent").replace(" ","")
    binding = ""
    if eval(isMandatory):
        binding = "ExternalAlgoProperties[(i:Description){}-{}].Value".format(attributeName,pName)
    else:
        binding = "Binding Path=ExternalAlgoProperties[(i:Description){}-{}].Value, ValidatesOnDataErrors=True, ValidatesOnExceptions=True".format(attributeName,pName)
    editable = "Binding Path=ExternalAlgoProperties[(i:Description){}-{}].IsEditable".format(attributeName,pName)
    parent = dom.createElement("TextBox")
    parent.setAttribute('Grid.Row', str(row))
    parent.setAttribute('Grid.Column', str(col))
    parent.setAttribute('x:Name', pName)
    parent.setAttribute('Style', "{StaticResource BasicStyle}")
    parent.setAttribute('IsEnabled', "{" + editable + "}")
    if visibility != "Visible":
        parent.setAttribute('Visibility',visibility)

    if eval(isMandatory):
        child = dom.createElement("TextBox.Text")
        firstChild = dom.createElement("Binding")
        firstChild.setAttribute('Path', binding)
        firstChild.setAttribute('ValidatesOnDataErrors', 'True')
        firstChild.setAttribute('ValidatesOnExceptions', 'True')
        firstChild.setAttribute('UpdateSourceTrigger', 'PropertyChanged')
        child.appendChild(firstChild)
        secondChild = dom.createElement("Binding.ValidationRules")
        firstChild.appendChild(secondChild)
        thirdChild = dom.createElement("i:ValueEmptyValidationRule")
        thirdChild.setAttribute('ElementId', pName)
        thirdChild.setAttribute('ValidatesOnTargetUpdated', 'True')
        secondChild.appendChild(thirdChild)
        parent.appendChild(child)
    else:
        parent.setAttribute('Text', "{" + binding + "}")

    return parent
