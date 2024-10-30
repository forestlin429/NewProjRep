import csv
import xml.etree.ElementTree as ET

def csv_to_xml(csv_file_path, xml_file_path):
    # Create the root element
    root = ET.Element("root")

    # Read the CSV file
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Create an item element for each row
            item = ET.Element("item")
            root.append(item)
            for key, value in row.items():
                # Create a child element for each field
                child = ET.Element(key)
                child.text = value
                item.append(child)

    # Create the tree and write to the XML file
    tree = ET.ElementTree(root)
    tree.write(xml_file_path)

# Example usage
csv_file_path = "C:/Temp/Rep/NewProj/data.csv"
xml_file_path = "C:/Temp/Rep/NewProj/output.xml"
csv_to_xml(csv_file_path, xml_file_path)