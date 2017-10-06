class Call(object):
    """docstring forMathDojo."""
    def __init__(self, id_number, caller_name, caller_number, time_of_call, reason_of_call):
        self.id_number = id_number
        self.caller_name = caller_name
        self.caller_number = caller_number
        self.time_of_call = time_of_call
        self.reason_of_call = reason_of_call

    def display(self):
        print self.id_number
        print self.caller_name
        print self.time_of_call
        print self.reason_of_call
        return self

class CallCenter(object):
    def __init__(self, calls = [], que_size =0):
        self.calls = calls
        self.que_size = que_size

    def add(self, call):
        self.calls.append(call)
        # self.remove(self, n = 0)
        # print "added"
        return self

    def remove(self, n = 0):
        del self.calls[n]
        # print "removed"
        return self

    def info(self):
        for i in self.calls:
            print i.caller_name
            print i.caller_number
            print self.calls.index(i)+1


joseph = Call(1231, "joseph", "310-123", "12:00", "cancer")
jane = Call(1211, "jane", "216-123", "11:00", "cancer")
call1 = CallCenter()
call1.add(joseph).add(joseph).remove().add(jane).info()
# CallCenter().info()
# print call1.add(joseph).calls[2].caller_name
# print call1.add(joseph).calls[1].caller_name
# print call1.add(joseph).calls[0].caller_name
