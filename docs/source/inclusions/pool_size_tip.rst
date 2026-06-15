.. tip::
    When making requests to the Bot API in an asynchronous fashion (e.g. via
    :attr:`block=False <fariks.ext.BaseHandler.block>`, :meth:`Application.create_task <fariks.ext.Application.create_task>`,
    :meth:`~fariks.ext.ApplicationBuilder.concurrent_updates` or the :class:`~fariks.ext.JobQueue`), it can happen that more requests
    are being made in parallel than there are connections in the pool.
    If the number of requests is much higher than the number of connections, even setting
    :meth:`~fariks.ext.ApplicationBuilder.pool_timeout` to a larger value may not always be enough to prevent pool
    timeouts.
    You should therefore set :meth:`~fariks.ext.ApplicationBuilder.concurrent_updates`, :meth:`~fariks.ext.ApplicationBuilder.connection_pool_size` and
    :meth:`~fariks.ext.ApplicationBuilder.pool_timeout` to values that make sense for your setup.