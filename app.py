from Model.test_model import MyModel
from Presenter.MainPresenter import MyPresenter
# from View.Customer import MyView
from View.MainWindowView import Ui_MainWindow


class test(object):

    def __init__(self):

        test_model = MyModel()
        test_view = Ui_MainWindow()




        self.presenter = MyPresenter(test_model, test_view)
