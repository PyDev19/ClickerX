#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QIcon>

int main(int argc, char *argv[]) {
    QGuiApplication app(argc, argv);
	app.setWindowIcon(QIcon(":/icons/icon.ico"));

    QQmlApplicationEngine engine;

    engine.load(QUrl(":/qml/Main.qml"));

    return app.exec();
}