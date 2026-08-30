try:
    import pymysql
    pymysql.install_as_MySQLdb()
    # Django 6.0's MySQL backend requires mysqlclient >= 2.2.1 and checks the
    # shim's version_info. PyMySQL reports its own version (e.g. 1.4.6), which
    # fails that check. Advertise a compatible version so Django accepts the
    # pure-Python driver (no C compilation needed on shared hosting).
    import MySQLdb
    MySQLdb.version_info = (2, 2, 1, 'final', 0)
    MySQLdb.__version__ = "2.2.1"
except ImportError:
    pass
