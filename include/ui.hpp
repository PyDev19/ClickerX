#ifndef UI_HPP
#define UI_HPP

#include <QQmlEngine>
#include <QQmlComponent>


class UI {
private:
    QQmlEngine& engine;
    QObject* root_object;
    QQmlComponent number_field_component;

public:
    QObject* row_layout;

    UI(QQmlEngine& engine, QObject* root_object);
    int setup_ui();
};

#endif