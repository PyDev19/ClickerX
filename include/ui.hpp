#ifndef UI_HPP
#define UI_HPP

#include <QQmlEngine>
#include <QQmlComponent>
#include <QObject>
#include <QQuickItem>

class UI: public QObject {
    Q_OBJECT
private:
    QQmlEngine& engine;
    QObject* root_object;
    QQmlComponent number_field_component;

public:
    QObject* row_layout;
    QHash<QString, QQuickItem*> number_fields;

    explicit UI(QQmlEngine &engine, QObject* parent = nullptr);
    int setup_ui(QObject* root_object);
};

#endif