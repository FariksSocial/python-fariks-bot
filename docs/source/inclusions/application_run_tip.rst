.. tip::
    * When combining ``python-fariks-bot`` with other :mod:`asyncio` based frameworks, using this
      method is likely not the best choice, as it blocks the event loop until it receives a stop
      signal as described above.
      Instead, you can manually call the methods listed below to start and shut down the application
      and the :attr:`~fariks.ext.Application.updater`.
      Keeping the event loop running and listening for a stop signal is then up to you.
    * To gracefully stop the execution of this method from within a handler, job or error callback,
      use :meth:`~fariks.ext.Application.stop_running`.