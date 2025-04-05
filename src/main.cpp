#include <QGuiApplication>
#include <QIcon>
#include <QObject>
#include <QQmlApplicationEngine>
#include <QQmlContext>


#include "keylistener.h"

int main(int argc, char *argv[]) {
    QGuiApplication app(argc, argv);
    app.setWindowIcon(QIcon(":/icons/icon.ico"));

    KeyListener key_listener;

    QQmlApplicationEngine engine;

    engine.rootContext()->setContextProperty("key_listener", &key_listener);

    engine.load(QUrl("qrc:/qml/Main.qml"));

    return app.exec();
}