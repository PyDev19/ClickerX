#include <QGuiApplication>
#include <QIcon>
#include <QObject>
#include <QQmlApplicationEngine>
#include <QQmlContext>


#include "cursorhandler.h"
#include "keylistener.h"

int main(int argc, char *argv[]) {
    QGuiApplication app(argc, argv);
    app.setWindowIcon(QIcon(":/icons/icon.ico"));

    KeyListener key_listener;
    CursorHandler cursor_handler;

    QQmlApplicationEngine engine;

    engine.rootContext()->setContextProperty("key_listener", &key_listener);
    engine.rootContext()->setContextProperty("cursor_handler", &cursor_handler);

    engine.load(QUrl("qrc:/qml/Main.qml"));

    return app.exec();
}