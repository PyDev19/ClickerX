#include <QQmlApplicationEngine>
#include <QGuiApplication>

int main (int argc, char *argv[]) {
	QGuiApplication app(argc, argv);
	
	QQmlApplicationEngine engine;

	engine.load(QUrl("qrc:qml/main.qml"));

	QList<QObject*> root_objects = engine.rootObjects();
	if (root_objects.isEmpty()) return -1;

	return app.exec();
}