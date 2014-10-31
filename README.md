check_elasticsearch
===================

A very simple ElasticSearch cluster check for nagios.

It connects to the `/_cluster/health` API and renders the returned JSON array into Nagios elements.

Usage
=====

    check_elasticsearch -H <ES host> -p <ES http port>
