#include <QQmlApplicationEngine>
#include <QGuiApplication>
#include <QIcon>
#include <ui.hpp>

int main(int argc, char *argv[]) {
    QGuiApplication app(argc, argv);
	app.setWindowIcon(QIcon(":/icons/icon.ico"));

    QQmlApplicationEngine engine;

    engine.load(QUrl("qrc:qml/main.qml"));

    QList<QObject*> root_objects = engine.rootObjects();
    if (root_objects.isEmpty()) return -1;

    QObject* root_object = root_objects.first();

	UI ui(engine, root_object);
	if (ui.setup_ui() == -1) {
		return -1;
	}

    return app.exec();
}
