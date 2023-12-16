#include "ui.hpp"
#include <QQuickItem>

UI::UI(QQmlEngine &engine, QObject* parent): QObject(parent), engine(engine) {}

/**
 * @brief This function is used to setup the ui by dynamically creating qml components needed in the application
*/
int UI::setup_ui(QObject* _root_object) {
    root_object = _root_object;
    QQmlComponent number_field_component(&engine, QUrl("qrc:qml/components/NumberField.qml"));\

    row_layout = root_object->findChild<QObject*>("click_interval_layout");
    if (!row_layout) {
        qWarning("RowLayout not found!");
        return -1;
    }

    if (number_field_component.isError()) {
        qWarning() << "Error loading component:" << number_field_component.errors();
        return -1;
    }

    for (int i = 0; i < 4; i++) {
        QQuickItem* number_field_item = qobject_cast<QQuickItem*>(number_field_component.create());

        if (number_field_item) {
            QQmlEngine::setObjectOwnership(number_field_item, QQmlEngine::CppOwnership);
            number_field_item->setParentItem(qobject_cast<QQuickItem*>(row_layout));

            switch (i) {
                case 0: 
                    number_field_item->setProperty("placeholderText", "Hours");
                    number_field_item->setProperty("id", "hours");
                    number_fields["hours"] = number_field_item;
                    break;
                case 1:
                    number_field_item->setProperty("placeholderText", "Minutes");
                    number_field_item->setProperty("id", "minutes");
                    number_fields["minutes"] = number_field_item;
                    break;
                case 2:
                    number_field_item->setProperty("placeholderText", "Seconds");
                    number_field_item->setProperty("id", "seconds");
                    number_fields["seconds"] = number_field_item;
                    break;
                case 3:
                    number_field_item->setProperty("placeholderText", "Milliseconds");
                    number_field_item->setProperty("id", "milliseconds");
                    number_fields["milliseconds"] = number_field_item;
                    break;
            }
        } else {
            qWarning() << "Error creating NumberField instance";
        }
    }

    return 0;
}