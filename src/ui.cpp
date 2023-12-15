#include <ui.hpp>
#include <QQuickItem>

UI::UI(QQmlEngine &engine, QObject* root_object): engine(engine), root_object(root_object), number_field_component(&engine, QUrl("qrc:qml/components/NumberField.qml")) {}

int UI::setup_ui() {
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
                    break;
                case 1:
                    number_field_item->setProperty("placeholderText", "Minutes");
                    number_field_item->setProperty("id", "minutes");
                    break;
                case 2:
                    number_field_item->setProperty("placeholderText", "Seconds");
                    number_field_item->setProperty("id", "seconds");
                    break;
                case 3:
                    number_field_item->setProperty("placeholderText", "Milliseconds");
                    number_field_item->setProperty("id", "milliseconds");
                    break;
            }
        } else {
            qWarning() << "Error creating NumberField instance";
        }
    }

    return 0;
}